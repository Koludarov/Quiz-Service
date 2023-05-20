# Quiz Service

Это веб-сервис на Python, созданный с использованием FastAPI, который получает случайные вопросы для викторины из публичного API и сохраняет их в базе данных PostgreSQL с использованием Docker.

## Подготовка

Установите Docker и Docker Compose, если они еще не установлены.


## Настройка базы данных

База данных PostgreSQL будет запущена автоматически с использованием Docker Compose. Здесь вы можете настроить логин, пароль и имя базы данных PostgreSQL по вашему усмотрению. Для этого нужно изменить следующие значения в файле `docker-compose.yml`:

- `POSTGRES_USER`: имя пользователя для подключения к базе данных.
- `POSTGRES_PASSWORD`: пароль пользователя для подключения к базе данных.
- `POSTGRES_DB`: название базы данных.

## Начало работы

1. Клонируйте данный репозиторий:

   ```bash
   git clone https://github.com/Koludarov/Quiz-Service
   cd Audio-Service
    ```
2. Соберите и запустите Docker-контейнеры:
    
   ```bash
      docker-compose up -d
    ```
   Это запустит контейнер базы данных PostgreSQL и контейнер приложения FastAPI.


3. Подключитесь к FastAPI-приложению:

    Откройте веб-браузер и перейдите по адресу http://localhost:8000/docs, для того чтобы воспользоваться функционалом.
## API Endpoints
POST /questions
Получает случайные вопросы для викторины и сохраняет их в базе данных.

## Тело запроса

Тело запроса должно быть JSON-объектом с одним свойством:

`questions_num` (целое число): Количество вопросов для получения.
Пример:
   ```json
{
  "questions_num": 2
}
   ```
## Ответ

Ответ будет представлен в виде JSON-массива и будет содержать полученные вопросы для викторины.
Пример:
   ```json
{
  "total": 2,
  "items": [
    {
      "id": 1,
      "question_id": 52938,
      "question_text": "The days between this holiday & Yom Kippur are called the 10 Days of Penitence",
      "answer_text": "Rosh Hashanah",
      "created_at": "2022-12-30T19:00:05.228000+00:00"
    },
    {
      "id": 2,
      "question_id": 35881,
      "question_text": "In Norwegian this body part is the tommelfinger",
      "answer_text": "the thumb",
      "created_at": "2022-12-30T18:52:26.928000+00:00"
    }
  ]
}
   ```