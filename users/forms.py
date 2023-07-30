from django.contrib.auth.forms import UserCreationForm, \
                                      UserChangeForm
from users.models import User
from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(
        max_length=20,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Пароль'}))


class UserRegisterForm(UserCreationForm):
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
        required=False,
        label="Имя пользователя",
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Логин'}))
    email = forms.EmailField(
        label="email",
        widget=forms.EmailInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Эл.почта'}))
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Пароль'}))
    password2 = forms.CharField(
        label="Подтвердить пароль",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name',
                  'username', 'email', 'password1', 'password2',)


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
                   'placeholder': 'Логин',
                   'readonly': True}))
    email = forms.EmailField(
        label="Эл.почта",
        widget=forms.EmailInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Эл.почта',
                   'readonly': True}))
    image = forms.ImageField(
        required=False,
        label="Фото",
        widget=forms.FileInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Фото'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name',
                  'image', 'username', 'email',)


class UserRecoveryPasswordForm(forms.Form):
    email = forms.EmailField(
        label="email",
        widget=forms.EmailInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Ваш email'}))


class UserCreatNewPasswordForm(UserCreationForm):
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Пароль'}))
    password2 = forms.CharField(
        label="Подтвердите пароль",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ('password1', 'password2',)