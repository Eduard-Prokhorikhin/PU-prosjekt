from django.urls import path

from . import views

urlpatterns = [
    path('', views.profilePage, name='index'),
    path('login/', views.registerPage, name='login'),
    path('register/', views.loginPage, name='register'),
]