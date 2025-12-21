from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = 'Initialize database for production deployment'

    def handle(self, *args, **options):
        self.stdout.write('Starting database initialization...')
        
        # Run migrations
        self.stdout.write('Running migrations...')
        call_command('migrate', verbosity=1, interactive=False)
        
        # Create superuser if it doesn't exist
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            self.stdout.write('Creating admin user...')
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write(self.style.SUCCESS('Admin user created successfully'))
        else:
            self.stdout.write('Admin user already exists')
        
        self.stdout.write(self.style.SUCCESS('Database initialization completed'))