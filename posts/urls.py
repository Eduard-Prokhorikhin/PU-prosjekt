from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='posts'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('new_post/', views.new_post, name='new_post'),
    path('new_post/<int:pk>', views.new_post, name='new_post'),
    path('create_post/', views.create_post, name='create_post'),
    path('create_post/<int:pk>', views.create_post, name='create_post'),
    path('rent_product/<int:pk>', views.rent_product, name='rent_product'),
    path('renter_detail/<int:pk>', views.renter_detail, name='renter_detail'),
    path('rate_rental/<int:pk>', views.rate_rental, name='rate_rental'),
]
