from django.shortcuts import render
from django.http import HttpResponse

from posts.models import Post

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello World!</h1>")

def page1(request):

    context = {
        'title': 'Page 1',
        'content': 'This is the content of page 1',
    }

    return render(request, 'header.html', context=context)

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)

    context = {
        'post': post,
    }

    return render(request, 'post_detail.html', context=context)