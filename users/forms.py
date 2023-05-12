from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.db.models import CharField

from users.models import User
from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField(label="Логин", widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Имя пользователя'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                'placeholder': 'Пароль'}))
    field_order = ["username", "password"]


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(
        label="Имя",
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Имя'}))
    last_name = forms.CharField(
        label="Фамилия",
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Фамилия'}))
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Логин'}))
    email = forms.EmailField(
        label="Эл.почта",
        widget=forms.EmailInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Эл.почта'}))
    image = forms.ImageField(
        label="Фото",
        widget=forms.FileInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Фото'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email')
