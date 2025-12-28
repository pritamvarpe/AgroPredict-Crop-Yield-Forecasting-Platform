#!/usr/bin/env python
"""
Run migrations manually for Render deployment
"""
import os
import django
from django.core.management import execute_from_command_line

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agri_platform.settings')
    django.setup()
    
    print("Running migrations...")
    execute_from_command_line(['manage.py', 'migrate'])
    print("Migrations completed!")