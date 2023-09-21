from django.db import models

# Create your models here.

from django.contrib.auth.models import BaseUserManager, AbstractUser

from django.contrib.auth.models import AbstractUser
from django.db import models


# Custom user model
class UserManager(BaseUserManager):
    # create and saves a User with the given username, email and password.
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=False, default='')
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Add your custom fields here

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Add any additional required fields

    def __str__(self):
        return self.email