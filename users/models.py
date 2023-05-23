from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(null=True, blank=True, upload_to='images_users')
    # age = models.PositiveIntegerField(max_length=3, blank=True)
    # state = models.TextField(max_length=30, blank=True)
    # city = models.TextField(max_length=20, blank=True)

    def __str__(self):
        return f'Login: {self.username} ' \
               f'| Staff: {self.is_staff} ' \
               f'| Superuser: {self.is_superuser} '