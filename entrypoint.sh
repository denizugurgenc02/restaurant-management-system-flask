#!/bin/sh

DB_HOST=postgres
DB_PORT=5432

echo "Waiting for PostgreSQL to start..."
while ! nc -z $DB_HOST $DB_PORT; do
  sleep 0.1
done
echo "PostgreSQL started."

echo "Running database migrations (upgrade)..."
flask db upgrade

exec "$@"