import logging

from fastapi import FastAPI, Path, HTTPException

from app.db.questions import open_session, create_question, question_exists, get_question_by_idx
from app.misc.request import get_question_data
from app.models.questions import QuestionData, QuestionRequest, QuestionsListData

logger = logging.getLogger(__name__)

app = FastAPI()


@app.post("/questions")
def add_questions(request: QuestionRequest) -> QuestionsListData:
    """Запрос на добавления n-количества вопросов в БД"""
    questions = []
    session = open_session()
    while len(questions) < request.questions_num:
        question = get_question_data()
        existing_question = question_exists(question.question_id, session)
        if existing_question:
            logger.info(f'Получен существующий вопрос {question.question_id}')
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


@app.get("/questions/{idx}")
def get_question(idx: int = Path(..., description="Question ID")) -> QuestionData:
    """Получает вопрос по id из базы данных."""
    session = open_session()
    question = get_question_by_idx(idx, session)
    session.close()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return QuestionData(
        id=question.id,
        question_id=question.question_id,
        question_text=question.question_text,
        answer_text=question.answer_text,
        created_at=question.created_at
    )
