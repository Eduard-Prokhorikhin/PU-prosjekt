from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from account.managers import UserManager

class User(AbstractBaseUser):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    phone = models.CharField(max_length=200)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
        
    objects = UserManager()
    
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')

