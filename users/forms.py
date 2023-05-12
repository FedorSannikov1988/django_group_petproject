from django.contrib.auth.forms import UserCreationForm, UserChangeForm

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
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    field_order = ["username", "password"]


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email')
