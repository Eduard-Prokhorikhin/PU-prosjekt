from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from datetime import date
from django.contrib.auth.decorators import login_required

from fuzzywuzzy import fuzz
from .models import *
from .forms import NewPostForm

# Create your views here.


def index(request):

    initial_list = Post.objects
    search_list = Post.objects.values('title').distinct()
    search_input = request.GET.get('q')
    
    # category_filter =

    if (request.GET.get('q') == None):
        post_list = initial_list.all().order_by('status', '-pub_date')
    else:
        post_list = initial_list.none()
        for item in search_list['value']:
            score = fuzz.ratio(item, search_input)
            print(score)
            if score >= 30:
                post_list |= Post.objects.get(title=item)
        #post_list = initial_list.filter(
         #   title__contains=search_input).order_by('status', '-pub_date')

    context = {
        'title': 'Annonser',
        'post_list': post_list,
        'initial_list': initial_list.all(),
        'search_list': search_list.all()
    }

    return render(request, 'posts.html', context=context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    next = request.META.get('HTTP_REFERER')
    try:
        rental = Rental.objects.get(post=pk)

    except:
        rental = None

    context = {
        'post': post,
        'rental': rental,
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
        post.category = form.cleaned_data['category']
        if request.FILES.get('image'):
            post.image = form.cleaned_data['image']
        post.save()
        return redirect('/account/')
    else:
        Post.objects.create(
            title=post['title'],
            category=post['category'],
            text=post['text'],
            author=User.objects.get(pk=request.user.id),
            image=post['image'],
        )

    return HttpResponseRedirect('/posts/')


def renter_detail(request, pk):
    user = User.objects.get(pk=pk)
    next = request.META.get('HTTP_REFERER')
    user_posts = Post.objects.filter(
        author=user, status='AVAILABLE').order_by('-pub_date')

    context = {
        'user': user,
        'next': next,
        'user_posts': user_posts
    }

    return render(request, 'renter_detail.html', context=context)
