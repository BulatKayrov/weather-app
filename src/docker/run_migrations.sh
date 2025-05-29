#!/bin/bash

alembic revision --autogenerate -m "created all tables"
alembic upgrade head
echo "Migrations success"
