from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from posts.models import Post

def index(request):
    return render(request, 'page.html')

def rent_product(request, pk):
    Post.objects.filter(pk=pk).update(status='UNAVAILABLE')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def reset_all_availability(request):
    Post.objects.all().update(status='AVAILABLE')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
