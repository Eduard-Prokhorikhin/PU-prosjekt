from django.shortcuts import render
from django.http import HttpResponse

from posts.models import Post

# Create your views here.
def index(request):
    return render(request, 'page.html')
