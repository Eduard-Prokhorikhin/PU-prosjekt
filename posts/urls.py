from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='posts'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('new_post/', views.new_post, name='new_post'),
    path('new_post/<int:pk>', views.new_post, name='new_post'),
    path('create_post/', views.create_post, name='create_post'),
    path('create_post/<int:pk>', views.create_post, name='create_post'),
    path('renter_detail/<int:pk>', views.renter_detail, name='renter_detail'),
]
