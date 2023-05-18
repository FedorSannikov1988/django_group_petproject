from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from users.models import User
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from shop.models import SoftwareCategory, Software, DevelopmentTeam

# глобальные переменные/данные:

title_for_basic_template = 'Дипломный проект студентов GB'

data_for_basic_template = {
    "software_category": SoftwareCategory.objects.all(),
    "software_operating_systems": Software.objects.filter(category__name='Операционные системы'),
    "software_office": Software.objects.filter(category__name='Офисное ПО'),
    "software_antivirus_protection": Software.objects.filter(category__name='Антивирусная защита')
}


def login(request):
    title_login = 'Вход в учетную запись - '

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            # username = request.POST['username']
            # password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('users:my_account'))
        else:
            print(form.errors)
    else:
        form = UserLoginForm()

    context = {
        'form': form,
        'page_title': title_login + title_for_basic_template,
    }

    return render(request, 'login.html', context)


def register(request):
    title_register = 'Регистрация - '

    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
        'page_title': title_register + title_for_basic_template,
    }

    return render(request, 'register.html', context)


def my_account(request):
    title_my_account = 'Личный кабинет - '

    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:my_account'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)

    context = {
        'form': form,
        'page_title': title_my_account + title_for_basic_template,
    }

    return render(request, 'my_account.html', {**context, **data_for_basic_template})


def exit_my_account(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def delete_my_account(request, user=None):
    user.delete()
    return HttpResponseRedirect(reverse('index'))
