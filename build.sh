#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Initialize database
python manage.py init_db

# Collect static files
python manage.py collectstatic --noinput