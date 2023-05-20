from django.urls import path

from users.views import login, register, my_account, exit_my_account, delete_profile

app_name = 'users'

urlpatterns = [
    path("login/", login, name='login'),
    path("register/", register, name='register'),
    path("my_account/", my_account, name='my_account'),
    path("exit_my_account/", exit_my_account, name='exit_my_account'),
    path("delete_profile/", delete_profile, name='delete_profile'),
]
