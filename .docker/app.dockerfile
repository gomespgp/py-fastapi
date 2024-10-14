FROM python:3.11.4

RUN mkdir /usr/src/server
WORKDIR /usr/src/server

RUN apt update && \
    apt install -y postgresql-client

COPY ./server/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
