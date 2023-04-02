FROM python:3.10-slim-buster
LABEL maintainer="Eleni Mantzana <helena.mantzana@gmail.com>"

ENV POETRY_VERSION=1.4.0

RUN apt-get update --fix-missing

RUN addgroup --system pokemonapp --gid 1000 && \
    adduser --ingroup pokemonapp --uid 1000 --disabled-password --system pokemonapp

WORKDIR /usr/src/app/
COPY ./ /usr/src/app/

RUN pip3 install poetry
COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-root

RUN chown -R pokemonapp:pokemonapp /usr/src/app/

USER pokemonapp
WORKDIR /usr/src/app