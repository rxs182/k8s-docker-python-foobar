FROM python:3.9-bookworm

ENV REDIS_HOST=${REDIS_HOST}
ENV REDIS_PORT=${REDIS_PORT}
ENV REDIS_QUEUE_NAME=${REDIS_QUEUE_NAME}

RUN touch /var/log/app.log

COPY app/ /usr/app/

CMD python dummy.py