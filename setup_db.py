from django.http import HttpResponse
from django.core.management import call_command
from django.contrib.auth import get_user_model
import io

def setup_database(request):
    """Run migrations and setup database via web request"""
    output = io.StringIO()
    
    try:
        # Run migrations
        call_command('migrate', stdout=output, stderr=output)
        
        # Create superuser if doesn't exist
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            output.write("Admin user created successfully\n")
        else:
            output.write("Admin user already exists\n")
            
        result = output.getvalue()
        return HttpResponse(f"<pre>Database setup completed:\n\n{result}</pre>")
        
    except Exception as e:
        return HttpResponse(f"<pre>Error: {str(e)}\n\nOutput:\n{output.getvalue()}</pre>")