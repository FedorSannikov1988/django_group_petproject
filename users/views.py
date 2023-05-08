from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from users.models import User
from users.forms import UserLoginForm, UserRegisterForm

# глобальные переменные/данные:

title_for_basic_template = 'Дипломный проект студентов GB'


def login(request):

    title_login = 'Вход в учетную запись - '

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            #username = request.POST['username']
            #password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
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
        form = UserRegisterForm()

    context = {
        'form': form,
        'page_title': title_register + title_for_basic_template,
    }

    return render(request, 'register.html', context)
