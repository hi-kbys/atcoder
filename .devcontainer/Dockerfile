FROM python:3.8.2

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    PYSETUP_PATH="/opt/pysetup"

ENV PATH="$POETRY_HOME/bin:$PATH"

RUN apt-get -y update && \
    apt-get -y upgrade && \
    # apt-get install --no-install-recommends -y curl && \
    apt-get clean

RUN curl -sSL https://install.python-poetry.org/ | python3 -

# # install requirements
RUN poetry config virtualenvs.create false
COPY pyproject.toml poetry.lock ./
RUN poetry install

# FROM nikolaik/python-nodejs

# # install atcoder-cli
# RUN apt-get -y update \ 
#     && apt-get -y upgrade \
#     && DEBIAN_FRONTEND=noninteractive apt-get -y install chromium-driver \
#     && npm install -g atcoder-cli


