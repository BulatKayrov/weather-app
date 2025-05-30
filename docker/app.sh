#!/bin/bash

alembic revision --autogenerate -m "created all tables"
alembic upgrade head
echo "Migrations success"

gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
