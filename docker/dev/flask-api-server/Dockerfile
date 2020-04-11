FROM python:3.6-slim

ENV FLASK_APP app.py

RUN pip install Flask

WORKDIR /usr/src/app

CMD flask run --host=0.0.0.0