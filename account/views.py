from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from posts.models import Post

# Create your views here.
@login_required
def profilePage(request):
    context = {'posts': Post.objects.filter(author=request.user).order_by('-status', '-pub_date')}
    return render(request, 'profile.html', context)

def registerPage(request):
    form = CreateUserForm()
    message = ""
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created succesfully.')
            return redirect('login')
        else:
            text = str(form.errors.as_text)
            messages.error(request, text[text.find("[")+2:text.find("]")-1])           
        
    context = {'form':form}
    return render(request, 'register.html', context)

def loginPage(request):
    form = AuthenticationForm()
    message = ''
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                print("Hello You have been logged in")
                
                # redirects to page that sent you here or index
                str = request.GET.get('next')
                if str == None: str = 'index'
                return redirect(str)
            else:
                print("Login failed!")
                
    context = {'form':form}
    return render(request, 'login.html', context)

def logoutPage(request):
    logout(request)
    messages.success(request, 'Logges out succesfully')
    return redirect('login')

