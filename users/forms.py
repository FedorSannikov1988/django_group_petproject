from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User

'''
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
'''

# или другой вариант:

from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField(label="Логин")
    password = forms.CharField(max_length=10, widget=forms.PasswordInput)
    field_order = ["username", "password"]


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
