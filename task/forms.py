from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class loginForm(UserCreationForm):
	email = forms.EmailField(max_length=200, help_text='enter valid email')
	class Meta:
		model=User
		fields=('username','password')

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='enter valid email')
    class Meta:
        model=User
        fields=('username','email','password1', 'password2')

