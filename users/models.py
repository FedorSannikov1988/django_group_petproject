from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(null=True, blank=True, upload_to='images_users')
    
    def __str__(self):
        return f'Login: {self.username} ' \
               f'| Staff: {self.is_staff} ' \
               f'| Superuser: {self.is_superuser} '