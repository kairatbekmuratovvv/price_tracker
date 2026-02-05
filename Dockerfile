FROM python:alpine

WORKDIR /app

COPY . .

RUN pip install requirements.txt

CMD ["uvicorn", "app.main:app", "--reload"]