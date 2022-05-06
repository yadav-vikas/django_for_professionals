#base image
FROM python:3.9

#set env vars
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#workdir
WORKDIR /code

#install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

#files
COPY . /code/