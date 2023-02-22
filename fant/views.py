from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from posts.models import *

def index(request):
    return render(request, 'page.html')

@login_required
def rent_product(request, pk):
    post = Post.objects.get(pk=pk)
    if post.author==request.user:
        print("test")
        url= reverse('post_detail', args=[str(pk)])
        return redirect(url)
    else:
        Post.objects.filter(pk=pk).update(status='UNAVAILABLE')
        Rental.objects.create(
            post=post,
            renter=User.objects.get(pk=request.user.id),
            )
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

