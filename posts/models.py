from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from account.managers import UserManager
from django.utils import timezone
from django.conf import settings

class User(AbstractBaseUser):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    phone = models.CharField(max_length=200)
    # django REQUIRED FIELDS:
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
        
    objects = UserManager()
    class Meta:
        abstract = False
    
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
           
    
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')

