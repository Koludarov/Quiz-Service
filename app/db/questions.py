import logging
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models.questions import Question


logger = logging.getLogger(__name__)

load_dotenv()

db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")


def open_session():
    engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}/{db_name}')
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
