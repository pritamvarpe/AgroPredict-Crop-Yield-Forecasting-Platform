#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Run migrations step by step
echo "Creating migrations..."
python manage.py makemigrations --noinput

echo "Running migrations..."
python manage.py migrate --noinput

echo "Creating superuser..."
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin123')"

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Build completed successfully!"