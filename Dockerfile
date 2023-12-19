FROM python:3.11

ENV PYTHONDONTWRITEBYTHECODE 1
ENV PYTHONUNBUFFERED 1


RUN mkdir /code
WORKDIR /code

RUN pip install --upgrade pip

COPY . /code/

RUN pip install -r requirements.txt
