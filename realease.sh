#!/bin/bash
set -e
echo "Starting release process..."

# Apply database migrations
python manage.py migrate --noinput

# Create a superuser non-interactively if it doesn't exist
python manage.py create_initial_superuser

echo "Release process finished."