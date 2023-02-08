from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

# Create your views here.
def index(request):

    post_list = Post.objects.all()

    # To search for a specific post
    post_list = Post.objects.filter(title__contains='')

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
