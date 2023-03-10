from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import *
from .forms import *

# Create your views here.


def index(request):
    if (request.GET.get('search') == None):
        post_list = Post.objects.all().order_by('status', '-pub_date')
    else:
        post_list = Post.objects.filter(title__contains=request.GET.get(
            'search')).order_by('status', '-pub_date')
    # rental_list = Rental.objects.all().values_list('post')
    # print(rental_list)
    # To search for a specific post
    # post_list = Post.objects.filter(title__contains='')

    context = {
        'title': 'Annonser',
        'post_list': post_list,
    }

    return render(request, 'posts.html', context=context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    try:
        rental = Rental.objects.get(post=pk)

    except:
        rental = None

    context = {
        'post': post,
        'rental': rental
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

def renter_detail(request, pk):
    user = User.objects.get(pk=pk)
    next = request.META.get('HTTP_REFERER')
    user_posts = Post.objects.filter(author=user, status='AVAILABLE').order_by('-pub_date')
    
    context = {
        'user': user,
        'next': next,
        'user_posts': user_posts
    }

    return render(request, 'renter_detail.html', context=context)

@login_required
def rate_rental(request, pk):
    form = RateRentalForm()
    user = Rental.objects.get(pk=pk).post.author
    post = Rental.objects.get(pk=pk).post

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

            return redirect('/account/')
        else:
            messages.error(request, 'Could not rate rental.')

    return render(request, 'rate_rental.html', {'rental_id': pk})
