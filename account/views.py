from django.shortcuts import render, redirect
# from posts.models import *
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm


# Create your views here.
def profilePage(request):
    context = {}
    return render(request, 'profile.html', context)

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
            
        
    context = {'form':form}
    return render(request, 'register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'login.html', context)

