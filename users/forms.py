from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User
from django import forms

'''
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

'''


# или другой вариант:

class UserLoginForm(forms.Form):
    username = forms.CharField(label="Логин")
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    field_order = ["username", "password"]


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email')
