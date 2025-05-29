FROM python:3.13-bookworm

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app
WORKDIR /app

# Установка системных зависимостей
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Установка uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.local/bin/:$PATH"

# Копирование зависимостей и установка
COPY pyproject.toml .
RUN uv sync

# Порт приложения
EXPOSE 8000

# Команда запуска
CMD ["gunicorn", "main:app", \
    "--workers", "1", \
    "--worker-class", "uvicorn.workers.UvicornWorker", \
    "--bind", "0.0.0.0:8000", \
    "--timeout", "120", \
    "--log-level", "debug", \
    "--access-logfile", "-", \
    "--error-logfile", "-"]