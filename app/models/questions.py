from datetime import datetime
from typing import List, Any

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer)
    question_text = Column(String)
    answer_text = Column(String)
    created_at = Column(DateTime)


class QuestionData(BaseModel):
    id: int
    question_id: int
    question_text: str
    answer_text: str
    created_at: datetime


class QuestionRequest(BaseModel):
    questions_num: int


class QuestionsListData(BaseModel):
    total: int
    items: List[Any] = []
