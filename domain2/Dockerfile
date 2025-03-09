FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./

# Install Poetry
RUN pip install --no-cache-dir poetry

# Install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . .

CMD ["poetry", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8002"]
