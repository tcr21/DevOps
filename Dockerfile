# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app
COPY requirements.txt requirements.txt
RUN python3 -m venv venv
RUN . venv/bin/activate && pip install -r requirements.txt
COPY . .

CMD . venv/bin/activate && [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
