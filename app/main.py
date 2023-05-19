from fastapi import FastAPI

from app.db.questions import open_session, create_question, question_exists
from app.misc.request import get_question
from app.models.questions import QuestionData, QuestionRequest, QuestionsListData

app = FastAPI()


@app.post("/questions")
def get_questions(request: QuestionRequest) -> QuestionsListData:
    """Запрос на добавления n-количества вопросов в БД"""
    questions = []
    session = open_session()
    while len(questions) < request.questions_num:
        question = get_question()
        existing_question = question_exists(question.question_id, session)
        if existing_question:
            continue
        create_question(question, session)

        questions.append(
            QuestionData(
                id=question.id,
                question_id=question.question_id,
                question_text=question.question_text,
                answer_text=question.answer_text,
                created_at=question.created_at
            ))

        session.close()

    return QuestionsListData(
        total=len(questions),
        items=questions
    )
