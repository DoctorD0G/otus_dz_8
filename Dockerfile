FROM python:3.10-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install poetry

RUN poetry install --no-root

COPY . .

EXPOSE 8000
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
