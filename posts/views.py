from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

from .models import Post

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

def new_post(request):
    # Get user credentials

    context = {
        # 'user': user
        'date': date.today()
    }

    return render(request, 'new_post.html', context=context)
