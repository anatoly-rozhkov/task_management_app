FROM python:3.13

SHELL ["/bin/bash", "-eo", "pipefail", "-c"]

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

ENV POETRY_VERSION=2.1.1
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/app/poetry python3 && ln -s /app/poetry/bin/poetry /usr/local/bin/poetry

RUN poetry --version

ENV POETRY_HOME="/app/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1

WORKDIR /app

COPY ./pyproject.toml ./poetry.lock ./

RUN poetry install --no-root


COPY ./project/ ./src

EXPOSE 8080

WORKDIR /app/src

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8080"]