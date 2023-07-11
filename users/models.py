from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(null=True, blank=True, upload_to='images_users')
    is_verified_email = models.BooleanField(default=False)
    email = models.EmailField(unique=True, blank=False)

    def __str__(self):
        return f'Login: {self.username} ' \
               f'| Staff: {self.is_staff} ' \
               f'| Superuser: {self.is_superuser} '


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    class Meta:
        verbose_name_plural = "Подтвержденные/активированные аккаунты"
        verbose_name = "подтвержденные/активированные аккаунты"

    def __str__(self):
        return f"Chek email {self.user.email}"
