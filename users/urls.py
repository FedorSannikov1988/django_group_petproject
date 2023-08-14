from django.urls import path
from users.views import login_user, \
                        register, \
                        my_account, \
                        exit_my_account, \
                        delete_profile, \
                        email_verification, \
                        forgot_password, \
                        create_new_password, \
                        delete_user_confirmation

app_name = 'users'

urlpatterns = [
    path("login/", login_user,
         name='login_user'),
    path("register/", register,
         name='register'),
    path("my_account/", my_account,
         name='my_account'),
    path("exit_my_account/", exit_my_account,
         name='exit_my_account'),
    path("delete_profile/", delete_profile,
         name='delete_profile'),
    path("verify/<str:email>/<uuid:code>/",
         email_verification,
         name='email_verification'),
    path("forgot_password/", forgot_password,
         name='forgot_password'),
    path("create_new_password/<str:email>/<uuid:code>/",
         create_new_password,
         name='create_new_password'),
    path("delete_user_confirmation/",
         delete_user_confirmation,
         name='delete_user_confirmation'),
    path("verify/<str:email>/<uuid:code>/",
         email_verification,
         name='email_verification'),
]
