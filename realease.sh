#!/bin/bash
set -e
echo "Starting release process..."
python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser

