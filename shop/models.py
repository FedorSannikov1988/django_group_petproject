from phonenumber_field.modelfields import PhoneNumberField
from users.models import User
from django.db import models


class SoftwareCategory(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    description = models.TextField(max_length=2000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images_software_category')

    def __str__(self):
        return f'Category: {self.name} '


class Software(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    price = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(null=True, blank=True, upload_to='images_software')
    category = models.ForeignKey(to=SoftwareCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'Software: {self.name} ' \
               f'| Price: {self.price} ' \
               f'| Quantity : {self.quantity} ' \
               f'| Category : {self.category.name} '


class FeaturesSoftware(models.Model):
    description = models.TextField(max_length=5000, null=True, blank=True)
    operating_system = models.CharField(max_length=50, null=True, blank=True)
    video_card = models.TextField(max_length=1000, null=True, blank=True)
    hard_disk_mb = models.PositiveIntegerField(null=True, blank=True)
    min_ram_mb = models.PositiveIntegerField(null=True, blank=True)
    software = models.ForeignKey(to=Software, on_delete=models.CASCADE)

    def __str__(self):
        return f'Operating System: {self.operating_system} ' \
               f'| Video Card: {self.video_card} ' \
               f'| Hard disk MB: {self.hard_disk_mb} ' \
               f'| Min RAM MB: {self.min_ram_mb} '


class DevelopmentTeam(models.Model):
    firstname = models.CharField(max_length=20, null=False)
    lastname = models.CharField(max_length=20, null=True, blank=True)
    patronymic = models.CharField(max_length=20, null=True, blank=True)
    telephone = PhoneNumberField(null=True, blank=True, unique=True)
    mail = models.EmailField(null=True, blank=True, unique=True)
    role = models.TextField(max_length=200, null=True, blank=True)
    description_work = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images_development_team')

    def __str__(self):
        return f'Firstname: {self.firstname} ' \
               f'| Lastname: {self.lastname} ' \
               f'| Patronymic: {self.patronymic} '


class FAQ(models.Model):
    question = models.TextField(max_length=500, null=True, blank=False)
    answer = models.TextField(max_length=2500, null=True, blank=False)

    def __str__(self):
        return f'Question: {self.question} ' \
               f'| Answer: {self.answer} '


class CartQuerySet(models.QuerySet):

    def total_sum(self):
        return sum(cart.sum() for cart in self)

    def total_quantity(self):
        return sum(cart.quantity for cart in self)


class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    software = models.ForeignKey(to=Software, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = CartQuerySet.as_manager()

    def sum(self):
        return self.software.price * self.quantity

    def __str__(self):
        return f'Username: {self.user.username} ' \
               f'| Software: {self.software.name} '


def user_directory_path(instance, filename):
    return 'question_user/{0}_{1}/{2}_{3}'.format(instance.user_id, instance.user.username,
                                                  instance.question_timestamp, filename)


class UsersQuestions(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=False)
    userquestion = models.TextField(max_length=500, null=False, blank=False)
    question_timestamp = models.DateTimeField(auto_now_add=True, null=True)
    upload = models.FileField(upload_to=user_directory_path, null=True, blank=True)

    def __str__(self):
        return f'Question: {self.userquestion} ' \
               f'| Date Question: {self.question_timestamp} ' \
               f'| Upload: {self.upload}'
