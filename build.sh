#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run migrations using Python script
echo "Running migrations..."
python run_migrations.py

# Create superuser
echo "Creating superuser..."
python -c "import os, django; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agri_platform.settings'); django.setup(); from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin123') if not User.objects.filter(username='admin').exists() else print('Admin user already exists')"

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Build completed successfully!"