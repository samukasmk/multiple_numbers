FROM python:3.12.2-slim

ENV PYTHONUNBUFFERED=1 \
	PYTHONDONTWRITEBYTCODE=1 \
	PIP_NO_CACHE_DIR=off \
	PIP_DEFAULT_TIMEOUT=100 \
	POETRY_VERSION=1.8.0 \
	POETRY_HOME="/opt/poetry" \
	POETRY_VIRTUALENVS_CREATE=false

ENV	PATH="$PATH:$POETRY_HOME/bin"

RUN pip install -U pip
RUN apt update && apt upgrade -y && apt install --no-install-recommends -y curl
RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /home/app
COPY . /home/app

RUN groupadd app && useradd -g app app
RUN chown -R app:app /home/app

RUN poetry install

USER app

ENTRYPOINT ["multiple-numbers"]
