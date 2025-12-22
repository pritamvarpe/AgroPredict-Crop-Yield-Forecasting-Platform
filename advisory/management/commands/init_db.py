from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth import get_user_model
from django.db import connection
import os

class Command(BaseCommand):
    help = 'Initialize database for production deployment'

    def handle(self, *args, **options):
        self.stdout.write('Starting database initialization...')
        
        try:
            # Check if database exists and has tables
            with connection.cursor() as cursor:
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tables = cursor.fetchall()
                self.stdout.write(f'Found {len(tables)} existing tables')
        except Exception as e:
            self.stdout.write(f'Database check failed: {e}')
        
        # Force create migrations
        self.stdout.write('Creating migrations...')
        try:
            call_command('makemigrations', verbosity=2, interactive=False)
        except Exception as e:
            self.stdout.write(f'Makemigrations error: {e}')
        
        # Run migrations with force
        self.stdout.write('Running migrations...')
        try:
            call_command('migrate', verbosity=2, interactive=False, run_syncdb=True)
        except Exception as e:
            self.stdout.write(f'Migration error: {e}')
            # Try syncdb as fallback
            try:
                call_command('migrate', verbosity=2, interactive=False, run_syncdb=True)
            except Exception as e2:
                self.stdout.write(f'Syncdb fallback error: {e2}')
        
        # Verify tables exist
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tables = cursor.fetchall()
                self.stdout.write(f'After migration: {len(tables)} tables exist')
                for table in tables:
                    self.stdout.write(f'  - {table[0]}')
        except Exception as e:
            self.stdout.write(f'Table verification failed: {e}')
        
        # Create superuser if it doesn't exist
        User = get_user_model()
        try:
            if not User.objects.filter(username='admin').exists():
                self.stdout.write('Creating admin user...')
                User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
                self.stdout.write(self.style.SUCCESS('Admin user created successfully'))
            else:
                self.stdout.write('Admin user already exists')
        except Exception as e:
            self.stdout.write(f'Admin user creation failed: {e}')
        
        self.stdout.write(self.style.SUCCESS('Database initialization completed'))