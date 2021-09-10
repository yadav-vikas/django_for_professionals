#base
FROM python:3.7

#env var
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#workdir
WORKDIR /code

#installing dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

#project files
COPY . /code/