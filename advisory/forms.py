from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import FarmInput, Contact

class FarmInputForm(forms.ModelForm):
    class Meta:
        model = FarmInput
        fields = '__all__'
        exclude = ['created_at']
        
        widgets = {
            'district': forms.Select(attrs={'class': 'form-select'}),
            'crop': forms.Select(attrs={'class': 'form-select'}),
            'season': forms.Select(attrs={'class': 'form-select'}),
            'sowing_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'field_area': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0.01'}),
            'irrigation': forms.Select(attrs={'class': 'form-select'}),
            'soil_type': forms.Select(attrs={'class': 'form-select'}),
            'soil_health_card': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'seed_variety': forms.Select(attrs={'class': 'form-select'}),
            'pest_presence': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
        labels = {
            'district': 'District',
            'crop': 'Crop Type',
            'season': 'Growing Season',
            'sowing_date': 'Sowing Date',
            'field_area': 'Field Area (hectares)',
            'irrigation': 'Irrigation Type',
            'soil_type': 'Soil Type',
            'soil_health_card': 'Soil Health Card Available?',
            'seed_variety': 'Seed Variety',
            'pest_presence': 'Pest/Disease Present?',
        }

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your.email@example.com'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject of your message'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Tell us how we can help you...'}),
        }
