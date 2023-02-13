from django.db import models


class User(models.Model):
    name = models.EmailField(max_length=200, unique=True)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    password = models.CharField(max_length=200, default="password")

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')

