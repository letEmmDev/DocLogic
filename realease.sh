#!/bin/bash
set -e
echo "Starting release process..."

# Apply database migrations
python manage.py migrate --noinput

# Create a superuser non-interactively
python manage.py createsuperuser --noinput

echo "Release process finished."