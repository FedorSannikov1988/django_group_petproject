import re
from datetime import datetime

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
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
    field_order = ("username", "password",)


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

    surname = forms.CharField(
        required=False,
        label="Отчество",
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Отчество'}))
    phone = forms.CharField(
        label="Номер телефона",
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Номер телефона'}))
    birthday = forms.DateField(
        label="День рождения",
        widget=forms.DateInput(
            attrs={'class': 'form-control',
                   'placeholder': 'День рождения в формате гггг-мм-дд'}))
    gender = forms.CharField(
        label="Пол",
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Ваш пол'}))
    address = forms.CharField(
        label="Адрес",
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Ваш адрес'}))


    password1 = forms.CharField(
        label=("Пароль"),
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Пароль'}))
    password2 = forms.CharField(
        label=("Подтвердить пароль"),
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Подтвердите пароль'}))

    def clean_gender(self):
        gender = self.cleaned_data.get('gender')
        if gender != 'M' and gender != 'F' and gender != 'm' and gender != 'f':
            raise forms.ValidationError("Укажите пол используя одну из двух букв M или F!")
        return gender

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(r'^\d+$', phone):
            raise forms.ValidationError("Номер телефона должен состоять только из цифр!")
        return phone

    def clean_birthday(self):
        birthday = self.cleaned_data.get('birthday')
        today = datetime.now().date()
        days = (today - birthday).days
        if days < 6570:
            raise forms.ValidationError("Вам еще нет 18 лет, вы не можете совершать покупки...")
        return birthday

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'surname',
                  'username', 'email', 'phone', 'birthday', 'gender', 'address', 'password1', 'password2',)


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