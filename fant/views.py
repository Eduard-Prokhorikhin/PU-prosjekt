from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from posts.models import *

def index(request):
    return render(request, 'page.html')

@login_required
def rent_product(request, pk):
    post = Post.objects.get(pk=pk)
    Rental.objects.create(
        post=post,
        renter=User.objects.get(pk=request.user.id),
        )
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# def reset_all_availability(request):
#     Post.objects.all().update(status='AVAILABLE')
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
