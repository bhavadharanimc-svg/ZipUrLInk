FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:7860"]
