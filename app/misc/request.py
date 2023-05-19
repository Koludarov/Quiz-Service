import requests
from app.models.questions import Question


def get_question() -> Question:
    response = requests.get("https://jservice.io/api/random?count=1").json()
    question_data = response[0]
    question = Question(
        question_text=question_data['question'],
        answer_text=question_data['answer'])
    return question
