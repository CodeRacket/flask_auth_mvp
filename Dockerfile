
FROM python:3.11

WORKDIR /app

# Install system dependencies for psycopg2
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*


RUN pip install --no-cache-dir poetry

# Copy pyproject.toml and install deps
COPY pyproject.toml poetry.lock* ./
RUN poetry config virtualenvs.create false \
  && poetry install --no-root --no-interaction --no-ansi


COPY . .


# Create and use non-root user
RUN useradd -m appuser
USER appuser


EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:create_app()"]
