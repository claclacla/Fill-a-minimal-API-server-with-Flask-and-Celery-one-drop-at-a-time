FROM python:3.6-slim

RUN pip install celery

WORKDIR /usr/src/celery

COPY ./MockSMTP.py /usr/src/celery
COPY ./tasks.py /usr/src/celery

CMD celery -A tasks worker --loglevel=info