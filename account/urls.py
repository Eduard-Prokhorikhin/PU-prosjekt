from django.urls import path

from . import views

urlpatterns = [
    path('', views.profilePage, name='index'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('endRental/<int:pk>', views.endRental, name='endRental'),
]