from typing import re
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.conf import settings
from django.utils.timezone import now


class User(AbstractUser):
    image = models.ImageField(null=True, blank=True, upload_to='images_users')
    is_verified_email = models.BooleanField(default=False)
    email = models.EmailField(unique=True, blank=False)
    birthday = models.DateField(null=True, blank=False)
    gender = models.TextField(max_length=1, null=True, blank=False)
    phone = models.TextField(null=True, blank=True, unique=True)
    address = models.CharField(max_length=150, null=True, blank=True)

    # def clean_birthday(self):
    #     if self.birthday is not None and (self.birthday < 18 or self.birthday > 150):
    #         raise ValidationError("Возраст должен быть указан в диапозоне от 18 до 150!") # make validate function
    #
    # def clean_gender(self):
    #     if self.gender is not None and (self.gender.lower() != 'M' or self.gender.lower() != 'F'):
    #         raise ValidationError("Укажите пол используя одну из двух букв M или F!")
    #
    # def clean_phone(self):
    #     if not re.match(r'^\d+$', self.phone):
    #         raise ValidationError("Номер телефона должен состоять только из цифр!")

    def __str__(self):
        return f'Login: {self.username} ' \
               f'| Staff: {self.is_staff} ' \
               f'| Superuser: {self.is_superuser} '


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def send_verification_email(self):
        half_link = reverse("users:email_verification", kwargs={"email": self.user.email, "code": self.code})
        verification_link = f"{settings.DOMAIN_NAME}{half_link}"

        subject = f"Подтверждение учетной записи для {self.user.username}"

        message = "Для подтверждения учетной записи {} {} {} " \
                  "перейдите по ссылке: {} ".format(
                    self.user.first_name,
                    self.user.last_name,
                    self.user.username,
                    verification_link)

        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
        )

    def is_expired(self):
        return True if now() >= self.expiration else False

    class Meta:
        verbose_name_plural = "Подтвержденные/активированные аккаунты"
        verbose_name = "подтвержденные/активированные аккаунты"

    def __str__(self):
        return f"Chek email {self.user.email}"
