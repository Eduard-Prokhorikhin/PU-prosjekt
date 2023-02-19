from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from datetime import date
from django.contrib.auth.decorators import login_required

from .models import Post
from .models import User
from .forms import NewPostForm

# Create your views here.
def index(request):

    post_list = Post.objects.all().order_by('status', '-pub_date')

    # To search for a specific post
    # post_list = Post.objects.filter(title__contains='')

    context = {
        'title': 'Annonser',
        'post_list': post_list,
    }

    return render(request, 'posts.html', context=context)

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)

    context = {
        'post': post,
    }

    return render(request, 'post_detail.html', context=context)

@login_required
def new_post(request):

    if request.method == 'POST':
        form = NewPostForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    else:
        form = NewPostForm()

    return render(request, 'new_post.html', {'form': form})

@login_required
def create_post(request):
    form = NewPostForm(request.POST, request.FILES)
    form.is_valid()

    post = form.cleaned_data
    
    Post.objects.create(
        title=post['title'],
        text=post['text'],
        author=User.objects.get(pk=request.user.id), 
        image=post['image'],
    )

    return HttpResponseRedirect('/posts/')
