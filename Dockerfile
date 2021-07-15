FROM ubuntu:20.0.4

WORKDIR /app

COPY ./requirements.txt /

RUN pip install -r /requirements.txt