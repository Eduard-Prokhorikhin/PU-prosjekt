from django.db import models
from datetime import datetime
from PIL import Image
from io import BytesIO
from django.core.files import File


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published', default=datetime.now())
    status = models.CharField(max_length=200, choices=[('AVAILABLE', 'available'), ('UNAVAILABLE', 'unavailable')], default='AVAILABLE')
    image = models.ImageField(upload_to='productImages/', blank=True)

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
            img.save(thumb_io, 'jpeg', quality=5)
            new_image = File(thumb_io, name=image.name)
            return new_image
