from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(null=True, blank=True, upload_to='images_users')
    # image = models.ImageField(null=True, blank=True, upload_to='images_users', height_field='300', width_field='300')

    # age = models.PositiveIntegerField(max_length=3, blank=True)
    # state = models.TextField(max_length=30, blank=True)
    # city = models.TextField(max_length=20, blank=True)
