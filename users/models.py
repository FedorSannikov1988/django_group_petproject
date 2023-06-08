import django
from django.db import models
from django.contrib.auth.models import AbstractUser


# AbstractUser
class User(AbstractUser):
    image = models.ImageField(null=True, blank=True, upload_to='images_users')

    # password = models.CharField(max_length=128, verbose_name='password')
    # last_login = models.DateTimeField(blank=True, null=True, verbose_name='last login')
    # is_superuser = models.BooleanField(default=False,
    #                                      help_text='Designates that this user has all permissions without explicitly assigning them.',
    #                                      verbose_name='superuser status')
    # username = models.CharField(error_messages={'unique': 'A user with that username already exists.'},
    #                               help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
    #                               max_length=150, unique=True,
    #                               # validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
    #                               verbose_name='username')
    # first_name = models.CharField(blank=True, max_length=150, verbose_name='first name')
    # last_name = models.CharField(blank=True, max_length=150, verbose_name='last name')
    # email = models.EmailField(blank=True, max_length=254, verbose_name='email address')
    # is_staff = models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.',
    #                      verbose_name='staff status')
    # is_active = models.BooleanField(default=True,
    #                                   help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
    #                                   verbose_name='active')
    # # date_joined = models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')
    # # image = models.ImageField(blank=True, null=True, upload_to='images_users')
    # groups = models.ManyToManyField(blank=True,
    #                                   help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    #                                   related_name='user_set', related_query_name='user', to='auth.Group',
    #                                   verbose_name='groups')
    # user_permissions = models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set',
    #                         related_query_name='user', to='auth.Permission', verbose_name='user permissions')
    #
    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['first_name', 'last_name',
    #           'username', 'email', 'password1', 'password2']
    #
    # @property
    # def is_anonymous(self):
    #     """
    #     Always return False. This is a way of comparing User objects to
    #     anonymous users.
    #     """
    #     return False

    def __str__(self):
        return f'Login: {self.username} ' \
               f'| Staff: {self.is_staff} ' \
               f'| Superuser: {self.is_superuser} '