# syntax=docker/dockerfile:1.26
FROM python:3.14-slim

RUN useradd -r python

WORKDIR /app

RUN --mount=type=bind,source=pyproject.toml,dst=pyproject.toml \
    pip install --no-cache-dir --upgrade .

COPY app/ .

RUN chown -R python:python /app

USER 1000

CMD ["fastapi", "run", "main.py", "--port", "80"]
