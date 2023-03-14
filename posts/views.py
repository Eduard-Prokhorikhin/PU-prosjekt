from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from datetime import date, timedelta
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import NewPostForm, RentRequestForm
from django.contrib import messages

# Create your views here.
def index(request):

    post_list = Post.objects.all().order_by('-pub_date')
    rental_list = RentRequest.objects.all().values_list('post')

    context = {
        'title': 'Annonser',
        'post_list': post_list,
        'rental_list': rental_list,
    }

    return render(request, 'posts.html', context=context)

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    rentals, rentedDays = getRentedDays(post)

    context = {
        'post': post,
        'rentals': rentals,
        'rentedDays': rentedDays,
    }

    return render(request, 'post_detail.html', context=context)

def getRentedDays(post):
    rentedDays = []
    
    rentals = RentRequest.objects.filter(post=post)
    for rental in rentals:
        print(type(rental.start_date))
        delta = rental.end_date - rental.start_date
        
        for i in range(delta.days + 1):
            day = rental.start_date + timedelta(days=i)
            rentedDays.append(day.strftime("%Y-%m-%d"))

    tuple(rentedDays)

    return rentals, rentedDays

@login_required
def new_post(request, pk=None):

    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)

        if form.is_valid():
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    else:
        if pk:
            post = Post.objects.get(pk=pk)
            form = NewPostForm(instance=post)
        else:
            form = NewPostForm()

    return render(request, 'new_post.html', {'form': form, 'post_id': pk})

@login_required
def create_post(request, pk=None):
    form = NewPostForm(request.POST, request.FILES)
    form.is_valid()

    post = form.cleaned_data
    if pk and request.user.id == Post.objects.get(pk=pk).author.id:
        post = Post.objects.get(pk=pk)
        post.title = form.cleaned_data['title']
        post.text = form.cleaned_data['text']
        if request.FILES.get('image'):
            post.image = form.cleaned_data['image']
        post.save()
        return redirect('/account/')
    else:
        Post.objects.create(
            title=post['title'],
            text=post['text'],
            author=User.objects.get(pk=request.user.id), 
            image=post['image'],
        )

    return HttpResponseRedirect('/posts/')

@login_required
def rent_product(request, pk):
    form = RentRequestForm()
    if request.method == "POST":
        form = RentRequestForm(request.POST)
        if form.is_valid():
            post = Post.objects.get(pk=pk)
            rentedDays = []
            
            rentals = RentRequest.objects.filter(post=post)
            for rental in rentals:
                print(type(rental.start_date))
                delta = rental.end_date - rental.start_date
                
                for i in range(delta.days + 1):
                    day = rental.start_date + timedelta(days=i)
                    rentedDays.append(day)

            print("Rented days: ", rentedDays)
            tuple(rentedDays)
            RentRequest.objects.create(
                post= Post.objects.get(pk=pk),
                renter=User.objects.get(pk=request.user.id),
                start_date=form.cleaned_data['start_date'],
                end_date=form.cleaned_data['end_date'],
                description=form.cleaned_data['description'],
                status = "ACCEPTED", #må settes til pending
            )
            messages.success = "Forespørsel sendt inn"
            return redirect("/posts/")
        else:
            messages.error = "Ugyldig skjema"
    return render(request, 'rent_product.html', {'form': form})



        
