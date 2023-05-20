import unittest
import requests


class QuizServiceEndpointTest(unittest.TestCase):
    def setUp(self):
        # Инициализация перед каждым тестом
        self.base_url = "http://localhost:8000"  # Адрес сервера

    def test_post_questions(self):
        # Проверка получения списка вопросов
        url = f"{self.base_url}/questions"
        questions_num = 2
        payload = {
            "questions_num": questions_num
        }
        response = requests.post(url, json=payload)
        self.assertEqual(response.status_code, 200)  # Проверка успешного запроса
        data = response.json()['items']
        self.assertIsInstance(data, list)  # Проверка, что получен список
        self.assertEqual(len(data), questions_num)  # Проверка, что количество вопросов соответствует заданному числу

    def test_get_question(self):
        # Проверка получения конкретного вопроса
        question_id = 1  # ID вопроса, который уже существует
        url = f"{self.base_url}/questions/{question_id}"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)  # Проверка успешного запроса
        data = response.json()
        self.assertIsInstance(data, dict)  # Проверка, что получен объект вопроса
        self.assertEqual(question_id, data.get('id'))  # Проверка, что получен вопрос по запрошенному id


if __name__ == '__main__':
    unittest.main()
