from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.utils.timezone import now
from django.conf import settings
from django.urls import reverse
from django.db import models

email_confirmation_time_hours = \
    settings.EMAIL_CONFIRMATION_TIME_HOURS
password_recovery_time_hours = \
    settings.PASSWORD_RECOVERY_TIME_HOURS


class User(AbstractUser):
    image = models.ImageField(null=True, blank=True, upload_to='images_users')
    is_verified_email = models.BooleanField(default=False)
    email = models.EmailField(unique=True, blank=False)
    surname = models.CharField(max_length=150, blank=True)
    birthday = models.DateField(null=True, blank=False)
    gender = models.TextField(max_length=1, null=True, blank=False)
    phone = models.TextField(null=True, blank=False, unique=True)
    address = models.CharField(max_length=150, null=True, blank=False)

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
        half_link = reverse("users:email_verification",
                            kwargs={"email": self.user.email,
                                    "code": self.code})
        verification_link_email = f"{settings.DOMAIN_NAME}{half_link}"

        subject = \
            f"Подтверждение адреса электронной почты"
        message = \
            f"Для подтверждения адреса электронной " \
            f"почты в учетной записи: " \
            f"{self.user.first_name} {self.user.last_name} " \
            f"перейдите по ссылке: {verification_link_email} ." \
            f" Cсылка активна {email_confirmation_time_hours} " \
            f"часов с момента отправки данного письма."

        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
        )

    def is_expired(self):
        return True if now() >= self.expiration else False

    def __str__(self):
        return f"Chek email {self.user.email}"

    class Meta:
        verbose_name_plural = "Подтвержденные/активированные аккаунты"
        verbose_name = "подтвержденные/активированные аккаунты"


class PasswordRecovery(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()
    link_used = models.BooleanField(default=False)

    def send_password_recovery_email(self):
        half_link = reverse("users:create_new_password",
                            kwargs={"email": self.user.username,
                                    "code": self.code})
        password_recovery_link = f"{settings.DOMAIN_NAME}{half_link}"

        subject = \
            "Восстановление пароля учетной записи"
        message = \
            f"Для смены пароля перейдите " \
            f"по ссылке: {password_recovery_link} ."\
            f" Cсылка активна " \
            f"{password_recovery_time_hours} " \
            f"часов c момента отправки данного письма."

        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
        )

    def is_expired(self):
        return True if now() >= self.expiration else False

    def __str__(self):
        return f"Password recovery {self.user.username}"

    class Meta:
        verbose_name_plural = "Восстановление/сменя пароля к аккаунту"
        verbose_name = "восстановление/сменя пароля к аккаунту"
