FROM alpine

RUN apk add --update mongodb-tools netcat-openbsd
COPY ./mongo.sh .
RUN chmod 700 ./mongo.sh

COPY ./teachers.json .

ENTRYPOINT ["/bin/sh", "./mongo.sh"]