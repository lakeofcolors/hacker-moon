# Pull base image

FROM python:3.8

# Set environment variables

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /hacker-moon

COPY Pipfile Pipfile.lock /hacker-moon/
RUN pip install pipenv && pipenv install --system

COPY . /hacker-moon/
