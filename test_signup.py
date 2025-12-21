#!/usr/bin/env python
"""
Simple test script to verify signup functionality
"""
import os
import sys
import django

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agri_platform.settings')
django.setup()

from django.contrib.auth.models import User
from advisory.forms import SignupForm

def test_signup_form():
    """Test the signup form validation"""
    print("Testing SignupForm...")
    
    # Test valid data
    valid_data = {
        'username': 'testuser123',
        'email': 'test@example.com',
        'password1': 'TestPassword123!',
        'password2': 'TestPassword123!'
    }
    
    form = SignupForm(data=valid_data)
    if form.is_valid():
        print("✓ Form validation passed")
        # Don't actually save in test
        print("✓ Form would create user successfully")
    else:
        print("✗ Form validation failed:")
        for field, errors in form.errors.items():
            print(f"  {field}: {errors}")
    
    # Test invalid data (password mismatch)
    invalid_data = {
        'username': 'testuser456',
        'email': 'test2@example.com',
        'password1': 'TestPassword123!',
        'password2': 'DifferentPassword123!'
    }
    
    form2 = SignupForm(data=invalid_data)
    if not form2.is_valid():
        print("✓ Form correctly rejected mismatched passwords")
    else:
        print("✗ Form should have rejected mismatched passwords")

def test_user_creation():
    """Test direct user creation"""
    print("\nTesting direct user creation...")
    
    try:
        # Check if test user already exists
        if User.objects.filter(username='testuser_direct').exists():
            User.objects.filter(username='testuser_direct').delete()
            print("Cleaned up existing test user")
        
        user = User.objects.create_user(
            username='testuser_direct',
            email='direct@example.com',
            password='TestPassword123!'
        )
        print(f"✓ User created successfully: {user.username}")
        
        # Clean up
        user.delete()
        print("✓ Test user cleaned up")
        
    except Exception as e:
        print(f"✗ User creation failed: {e}")

if __name__ == '__main__':
    test_signup_form()
    test_user_creation()
    print("\nTest completed!")