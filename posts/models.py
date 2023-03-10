from django.db import models
from datetime import datetime
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.contrib.auth.models import AbstractBaseUser
from account.managers import UserManager
from django.utils import timezone
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class User(AbstractBaseUser):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    phone = models.CharField(max_length=200)
    rating = models.FloatField(default=5, validators=[MaxValueValidator(5), MinValueValidator(1)])
    rating_count = models.IntegerField(default=1)
    
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
           
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.is_active = False
        self.save()
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published', default=datetime.now())
    status = models.CharField(max_length=200, choices=[('AVAILABLE', 'available'), ('UNAVAILABLE', 'unavailable')], default='AVAILABLE')
    image = models.ImageField()
    rating = models.FloatField(default=5, validators=[MaxValueValidator(5), MinValueValidator(1)])
    rating_count = models.IntegerField(default=1)

    # before saving the instance we're reducing the image
    def save(self, *args, **kwargs):
        if self.image:
            new_image = self.reduce_image_size(self.image)
            self.image = new_image
        super().save(*args, **kwargs)
    def reduce_image_size(self, image):
        if image:
            img = Image.open(image)
            thumb_io = BytesIO()
            img.save(thumb_io, 'jpeg', quality=50)
            new_image = File(thumb_io, name=image.name)
            return new_image

class Rental(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    renter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)