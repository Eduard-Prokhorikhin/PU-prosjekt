from django.shortcuts import render, redirect
from posts.models import *

# Create your views here.
def profilePage(request):
    context = {}
    return render(request, 'profile.html', context)

def registerPage(request):
    context = {}
    return render(request, 'register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'login.html', context)

