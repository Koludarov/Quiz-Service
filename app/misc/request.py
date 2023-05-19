import requests
from app.models.questions import Question


def get_question() -> Question:
    response = requests.get("https://jservice.io/api/random?count=1").json()
    question_data = response[0]
    question = Question(
        question_id=question_data['id'],
        question_text=question_data['question'],
        answer_text=question_data['answer'],
        created_at=question_data['created_at']
    )
    return question
