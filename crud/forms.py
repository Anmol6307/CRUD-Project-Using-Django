from django import forms
from django.core import validators
from django.forms import widgets
from .models import User

class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
          'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Name'}),
          'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Your Email'}),
          'password': forms.PasswordInput(render_value=True, attrs={'class':'form-control', 'placeholder':'Enter Your Password'}),
        }
        
        
        