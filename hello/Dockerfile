#base image
FROM python:3.9

#env var
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#WORK DIRECTORY
WORKDIR /code

#dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv
RUN pipenv install --system

#copy files
COPY . /code/