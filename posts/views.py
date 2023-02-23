from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from datetime import date
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import NewPostForm

# Create your views here.
def index(request):

    post_list = Post.objects.all().order_by('status', '-pub_date')
    rental_list = Rental.objects.all().values_list('post')
    print(rental_list)
    # To search for a specific post
    # post_list = Post.objects.filter(title__contains='')

    context = {
        'title': 'Annonser',
        'post_list': post_list,
        'rental_list': rental_list,
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
        'rental': rental,
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
