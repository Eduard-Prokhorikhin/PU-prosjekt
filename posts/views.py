from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from datetime import date, timedelta
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.


def index(request):
    initial_list = Post.objects

    search_input = request.GET.get('q')

    if (request.GET.get('q') == None):
        post_list = initial_list.all().order_by('-pub_date')
    else:
        post_list = initial_list.filter(
            title__contains=search_input).order_by('-pub_date')

    # rental_list = Rental.objects.all().values_list('post')
    # print(rental_list)
    # To search for a specific post
    # post_list = Post.objects.filter(title__contains='')

    context = {
        'title': 'Annonser',
        'post_list': post_list,
        'initial_list': initial_list.all(),
    }

    return render(request, 'posts.html', context=context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    rentals, rentedDays = getRentedDays(post)
    next = request.META.get('HTTP_REFERER')

    context = {
        'post': post,
        'rentals': rentals,
        'rentedDays': rentedDays,
        'next': next
    }

    return render(request, 'post_detail.html', context=context)


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
    post = Post.objects.get(pk=pk)
    rentals, rentedDays = getRentedDays(post)

    form = RentRequestForm()
    if request.method == "POST":
        form = RentRequestForm(request.POST)
        if form.is_valid():
            days = daysInBetween(form.cleaned_data['start_date'], form.cleaned_data['end_date'])
            for day in rentedDays:
                if day in days:
                    messages.success(request, "Datoen er opptatt")
                    return redirect(request.META.get('HTTP_REFERER'))
            
            RentRequest.objects.create(
                post= Post.objects.get(pk=pk),
                renter=User.objects.get(pk=request.user.id),
                start_date=form.cleaned_data['start_date'],
                end_date=form.cleaned_data['end_date'],
                description=form.cleaned_data['description'],
                status = "PENDING", #må settes til pending
            )
            messages.success(request, "Forespørsel sendt inn")
            return redirect("/posts/")
        else:
            messages.error(request, "Ugyldig skjema")

    context = {
        'form': form,
        'rentedDays': rentedDays
    }

    return render(request, 'rent_product.html', context=context)



# Functions
def getRentedDays(post):
    rentedDays = []
    
    rentals = RentRequest.objects.filter(post=post, status="ACCEPTED")
    for rental in rentals:
        delta = rental.end_date - rental.start_date
        
        for i in range(delta.days + 1):
            day = rental.start_date + timedelta(days=i)
            rentedDays.append(day.strftime("%Y-%m-%d"))

    tuple(rentedDays)

    return rentals, rentedDays

def daysInBetween(start, end):
    days = []
    delta = end - start
    for i in range(delta.days + 1):
        day = start + timedelta(days=i)
        days.append(day.strftime("%Y-%m-%d"))
    return days

def renter_detail(request, pk):
    user = User.objects.get(pk=pk)
    next = request.META.get('HTTP_REFERER')
    user_posts = Post.objects.filter(author=user).order_by('-pub_date')
    
    context = {
        'user': user,
        'next': next,
        'user_posts': user_posts
    }

    return render(request, 'renter_detail.html', context=context)

@login_required
def rate_rental(request, pk):
    form = RateRentalForm()
    user = RentRequest.objects.get(pk=pk).post.author
    post = RentRequest.objects.get(pk=pk).post

    context = {
        'form': form,
        'user': user,
        'post': post
    }

    if request.method == 'POST':
        form = RateRentalForm(request.POST)
        if form.is_valid():
            user_initialrating = user.rating
            user.rating = (user_initialrating * user.rating_count + form.cleaned_data['user_rating']) / (user.rating_count+1)
            user.rating_count += 1
            user.save()

            post_initialrating = post.rating
            post.rating = (post_initialrating * post.rating_count + form.cleaned_data['post_rating']) / (post.rating_count+1)
            post.rating_count += 1
            post.save()
            RentRequest.objects.filter(pk=pk).update(review=True)

            return redirect('/account/')
        else:
            messages.error(request, 'Could not rate rental.')

    return render(request, 'rate_rental.html', {'rental_id': pk})
