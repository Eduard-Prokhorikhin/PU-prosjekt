from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from posts.models import *

# Create your views here.
@login_required
def profilePage(request):
    context = {
        'rent_requests' : RentRequest.objects.filter(post__in=Post.objects.filter(author=request.user), status= 'PENDING').order_by('-end_date'),
        'rentals': RentRequest.objects.filter(renter=request.user, review=False).exclude(status='REJECTED').order_by('-start_date'),
        'posts': Post.objects.filter(author=request.user).order_by('-pub_date'),
        'history': RentRequest.objects.filter(renter=request.user, status='ACCEPTED', review=True).order_by('-end_date'),
    }
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
                adress = request.GET.get('next')
                if adress == None: adress = 'index'
                return redirect(adress)
            else:
                print("Login failed!")
                
    context = {'form':form}
    return render(request, 'login.html', context)

def logoutPage(request):
    logout(request)
    messages.success(request, 'Logged out succesfully')
    return redirect('login')

def endRental(request, pk):
    rental= RentRequest.objects.get(pk=pk)
    if rental.start_date > datetime.now().date():
        messages.error(request, "Kan ikke avslutte leie før startdato av forholdet")
        return redirect('index')
    else:
        RentRequest.objects.filter(pk=pk).update(end_date= datetime.now().date())
        return redirect('rate_rental', pk=pk)

def acceptRental(request, pk):
    RentRequest.objects.filter(pk=pk).update(status="ACCEPTED")
    return redirect('index')

def rejectRental(request, pk):
    RentRequest.objects.filter(pk=pk).update(status="REJECTED")
    return redirect('index')

