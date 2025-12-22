#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Initialize database with enhanced command
echo "Initializing database..."
python manage.py init_db

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Build completed successfully!"