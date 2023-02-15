from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms



class CreateUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['firstname', 'lastname', 'phone', 'email']

# class LogInForm(AuthenticationForm):
#     email = forms.CharField(max_length=63)
#     password = forms.CharField(max_length=63, widget=forms.PasswordInput)