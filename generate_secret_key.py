import secrets
import string

def generate_secret_key():
    """Generate a secure Django SECRET_KEY"""
    chars = string.ascii_letters + string.digits + '!@#$%^&*(-_=+)'
    return ''.join(secrets.choice(chars) for _ in range(50))

if __name__ == '__main__':
    secret_key = generate_secret_key()
    print("Your new SECRET_KEY:")
    print(secret_key)
    print("\nAdd this to your Render environment variables:")
    print(f"SECRET_KEY={secret_key}")