FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /app

ENV PATH="/root/.local/bin:${PATH}"
ENV PYTHONPATH="/app"
ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_HTTP_TIMEOUT=120

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
