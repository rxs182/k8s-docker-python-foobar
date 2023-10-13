FROM python:3.9-bookworm

ENV REDIS_HOST=${REDIS_HOST}
ENV REDIS_PORT=${REDIS_PORT}
ENV REDIS_QUEUE_NAME=${REDIS_QUEUE_NAME}

RUN apt update -y && apt install -y openjdk-17-jdk


RUN touch /var/log/app.log

COPY app/ /usr/app/
COPY lib/ /usr/lib/

WORKDIR /usr/lib/demo
RUN ./mvnw clean install -Dmaven.test.skip=true

WORKDIR /usr/app
RUN javac Main.java

CMD python main.py