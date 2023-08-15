from django.contrib.auth.forms import UserCreationForm, \
                                      UserChangeForm
from django.utils.timezone import now
from users.models import User
from django import forms
import re

MIN_AGE_MAKING_TRANSACTION_DAYS: int = 6570
MAX_LEN_PASS: int = 30


class UserLoginForm(forms.Form):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Адрес электронной почты'}))
    password = forms.CharField(
        max_length=MAX_LEN_PASS,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Пароль'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        required=False,
        label="Логин",
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Логин'}))
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
    surname = forms.CharField(
        required=False,
        label="Отчество",
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Отчество'}))
    email = forms.EmailField(
        label="email",
        widget=forms.EmailInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Эл.почта'}))
    phone = forms.CharField(
        label="Номер телефона",
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Номер телефона'}))
    birthday = forms.DateField(
        label="День рождения",
        widget=forms.DateInput(
            attrs={'class': 'form-control',
                   'placeholder':
                       'День рождения в '
                       'формате гггг-мм-дд'}))
    gender = forms.CharField(
        label="Пол",
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Ваш пол (М/Ж)'}))
    address = forms.CharField(
        label="Адрес",
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Ваш адрес '
                                  '(не более 150 символов)'}))
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

    def clean_gender(self):
        gender = self.cleaned_data.get('gender')
        if gender != 'М' and gender != 'Ж':
            text_error: str = \
                "Укажите пол используя одну " \
                "из двух букв верхнего регистра " \
                "М или Ж!"
            raise forms.ValidationError(text_error)
        return gender

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(r'^\d+$', phone):
            text_error: str = \
                "Номер телефона должен состоять " \
                "только из цифр!"
            raise forms.ValidationError(text_error)
        return phone

    def clean_birthday(self):
        birthday = self.cleaned_data.get('birthday')
        days = (now().date() - birthday).days
        if days < MIN_AGE_MAKING_TRANSACTION_DAYS:
            text_error: str = \
                "Вам еще нет 18 лет, вы не можете " \
                "совершать покупки в нашем магазине"
            raise forms.ValidationError(text_error)
        return birthday

    class Meta:
        model = User
        fields = ('first_name', 'last_name',
                  'surname', 'username',
                  'email', 'phone',
                  'birthday', 'gender',
                  'address', 'password1',
                  'password2',)


class UserProfileForm(UserChangeForm):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Логин',
                   'readonly': True}))
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
    surname = forms.CharField(
        required=False,
        label="Отчество",
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Отчество'}))
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
    phone = forms.CharField(
        label="Номер телефона",
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Номер телефона'}))
    birthday = forms.DateField(
        label="День рождения",
        widget=forms.DateInput(
            attrs={'class': 'form-control',
                   'placeholder': 'День рождения в '
                                  'формате гггг-мм-дд'}))
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

    class Meta:
        model = User
        fields = ('first_name', 'last_name',
                  'username', 'image',
                  'email', 'surname',
                  'phone', 'birthday',
                  'gender', 'address',)


class UserRecoveryPasswordForm(forms.Form):
    email = forms.EmailField(
        label="email",
        widget=forms.EmailInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Ваш email'}))


class UserCreatNewPasswordForm(forms.Form):
    password1 = forms.CharField(
        max_length=MAX_LEN_PASS,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Пароль'}))
    password2 = forms.CharField(
        max_length=MAX_LEN_PASS,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Подтвердите пароль'}))
