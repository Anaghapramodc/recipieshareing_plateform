from django.db import models

from django.conf import settings


# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    preparation = models.TextField()
    image_url = models.ImageField(upload_to='pics')
    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    image_url = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name
