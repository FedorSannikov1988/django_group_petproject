import uuid
from datetime import timedelta

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from django.utils.timezone import now

from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from users.models import User, EmailVerification
from shop.views import title_for_basic_template, data_for_basic_template


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
        'page_title': title_login + title_for_basic_template(),
        'message_error': message_error,
        'form': form
    }
    return render(request, 'login.html', context)


def register(request):
    title_register = 'Регистрация - '

    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            username_form = form.save(commit=False)
            username_form.username = form.cleaned_data['email']
            username_form.save()
            user = User.objects.get(username=username_form.username)
            expiration = now() + timedelta(hours=48)
            record = EmailVerification.objects.create(code=uuid.uuid4(),
                                                      user=user,
                                                      expiration=expiration)
            record.send_verification_email()

            messages.success(request, 'Вы успешно зарегистрированы!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
        'page_title': title_register + title_for_basic_template()
    }
    return render(request, 'register.html', context)


def email_verification(request, email, code):
    title_register = 'Подтверждение адреса электронной почты - '

    user = User.objects.get(email=email)
    for_email_verification = EmailVerification.objects.filter(user=user,
                                                              code=code)

    if for_email_verification.exists() and \
            not for_email_verification.first().is_expired():
        user.is_verified_email = True
        user.save()
    else:
        return HttpResponseRedirect(reverse('index'))

    context = {
        'page_title': title_register + title_for_basic_template()
    }
    return render(request, 'email_verification.html', context)


def delete_user_confirmation(request):
    title_index = 'Подтверждение удаления - '

    context = {
        "page_title": title_index + title_for_basic_template()
    }
    return render(request, 'delete_user_confirmation.html', {**context, **data_for_basic_template(request)})


@login_required
def my_account(request):
    title_my_account = 'Личный кабинет - '

    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        # new_password = form.cleaned_data['password2']
        # user.set_password(new_password)
        # user.save()

        if form.is_valid():
            print('///////////////////')
            print(form)
            form.save()
            return HttpResponseRedirect(reverse('users:my_account'))
        else:
            print('**********')
            initial_data = {'username': request.user.email}
            form = UserProfileForm(instance=request.user, initial=initial_data)
            print(form)
            form.save()
            if form.is_valid():
                print('++++++++++++++++')
                form.save()
                return HttpResponseRedirect(reverse('users:my_account'))
            # print(form.cleaned_data['username'])
            # print(form.cleaned_data['first_name'])
            # print(form.cleaned_data['last_name'])
            # print(form.cleaned_data['email'])
            # print(form.cleaned_data['surname'])
            # print(form.cleaned_data['phone'])
            # print(form.cleaned_data['birthday'])
            # print(form.cleaned_data['gender'])
            # print(form.cleaned_data['address'])
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
    if User.objects.filter(username=user.username).exists():
        User.objects.all().filter(username=request.user.username).delete()
        auth.logout(request)
        return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
