from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from users.models import User
from shop.views import title_for_basic_template, data_for_basic_template
from django.core.exceptions import NON_FIELD_ERRORS


def login(request):
    title_login = 'Вход в учетную запись - '
    message_error = ''

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('users:my_account'))
            else:
                if User.objects.filter(username=username).exists():
                    message_error = 'Неверный пароль'
                else:
                    message_error = 'Учетной записи с таким именем пользователя нет в базе данных'
    else:
        form = UserLoginForm(data=request.POST)

    context = {
        'message_error': message_error,
        'form': form,
        'page_title': title_login + title_for_basic_template(),
    }
    return render(request, 'login.html', context)


def register(request):
    title_register = 'Регистрация - '

    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        # username_form = form.save(commit=False)
        # username_form.username = form.cleaned_data['email']
        flag = form.is_valid()
        if flag:
            # username_form.save()
            form.save()
            messages.success(request,'Вы успешно зарегистрированы!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
        'page_title': title_register + title_for_basic_template(),
    }
    return render(request, 'register.html', context)


@login_required
def my_account(request):
    title_my_account = 'Личный кабинет - '

    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:my_account'))
    else:
        form = UserProfileForm(instance=request.user)

    context = {
        'form': form,
        'page_title': title_my_account + title_for_basic_template(),
    }
    return render(request, 'my_account.html', {**context, **data_for_basic_template(request)})


@login_required
def exit_my_account(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def delete_profile(request):
    user = request.user
    if User.objects.filter(username=user).exists():
        User.objects.filter(username=user).delete()
        return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
