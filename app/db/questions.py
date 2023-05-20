import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models.questions import Question


logger = logging.getLogger(__name__)


def open_session():
    engine = create_engine('postgresql://postgres:postgres@db/quiz_service_db')
    Session = sessionmaker(bind=engine)
    session = Session()
    logger.info('Успешное подключение к БД')
    return session


def create_question(question: Question, session):
    session.add(question)
    session.commit()
    logger.info(f'Вопрос id {question.id} добавлен')


def question_exists(question_id: int, session):
    return session.query(Question).filter_by(question_id=question_id).first()


def get_question_by_idx(question_id: int, session):
    return session.query(Question).filter_by(id=question_id).first()
