#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Remove existing database to start fresh
echo "Removing existing database..."
rm -f db.sqlite3

# Create fresh migrations
echo "Creating migrations..."
python manage.py makemigrations advisory
python manage.py makemigrations

# Run migrations
echo "Running migrations..."
python manage.py migrate

# Create superuser
echo "Creating superuser..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin123') if not User.objects.filter(username='admin').exists() else None" | python manage.py shell

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Build completed successfully!"