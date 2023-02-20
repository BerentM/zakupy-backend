#!/bin/sh

# Check connection to db
while ! pg_isready --dbname=$POSTGRES_DB --host=$POSTGRES_URL --port=5432 --username=$POSTGRES_USER; do
  sleep 1
done

# Run migrations
python setup.py

# Start the backend...
uvicorn app.app:app --reload --workers 1 --host 0.0.0.0 --port 8000
