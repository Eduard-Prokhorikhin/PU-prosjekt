from django.forms import ModelForm
from posts.models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'phone', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user