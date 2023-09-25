FROM python:3.11

ENV POETRY_HOME="/opt/poetry"
ARG WORKDIR="/workspaces/atcoder"

ENV PATH="$POETRY_HOME/bin:$PATH"
ENV PATH="$PATH:$WORKDIR/.venv/bin"

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get clean

RUN curl -sSL https://install.python-poetry.org/ | python3 -

# # install requirements
RUN poetry config virtualenvs.in-project true
COPY pyproject.toml poetry.lock ./
RUN poetry install