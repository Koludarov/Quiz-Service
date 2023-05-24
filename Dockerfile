FROM python:3.9

WORKDIR /app

COPY requirements/base.txt .

RUN pip install --upgrade pip

RUN pip install -r base.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000","--log-config","etc/logging.conf"]
