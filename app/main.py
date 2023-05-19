from fastapi import FastAPI
import requests
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from pydantic import BaseModel

Base = declarative_base()


class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    question_text = Column(String)
    answer_text = Column(String)
    created_at = Column(DateTime, default=datetime.now)


class QuestionRequest(BaseModel):
    questions_num: int


app = FastAPI()


@app.post("/questions")
def get_questions(request: QuestionRequest):
    engine = create_engine('postgresql://postgres:postgres@db/quiz_db')
    Session = sessionmaker(bind=engine)
    session = Session()

    questions = []

    while len(questions) < request.questions_num:
        response = requests.get("https://jservice.io/api/random?count=1").json()
        question_data = response[0]
        question_text = question_data['question']
        answer_text = question_data['answer']

        existing_question = session.query(Question).filter_by(question_text=question_text).first()
        if existing_question:
            continue

        question = Question(question_text=question_text, answer_text=answer_text)
        session.add(question)
        session.commit()

        questions.append({
            "id": question.id,
            "question_text": question.question_text,
            "answer_text": question.answer_text,
            "created_at": question.created_at
        })

    session.close()
    return questions
