import uuid
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, \
                             HttpResponseRedirect
from django.contrib import auth, \
                           messages
from django.urls import reverse
from django.utils.timezone import now
from users.forms import UserLoginForm, \
                        UserRegisterForm, \
                        UserProfileForm, \
                        UserRecoveryPasswordForm, \
                        UserCreatNewPasswordForm
from users.models import User, \
                         EmailVerification, \
                         PasswordRecovery
from shop.views import title_for_basic_template, \
                       data_for_basic_template


def login(request):
    title_login: str = 'Вход в личный кабинет - '
    message_error: str = ''

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = auth.authenticate(username=username,
                                     password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('users:my_account'))
            else:
                if User.objects.filter(username=username).exists():
                    message_error = 'Неверный пароль'
                else:
                    message_error = 'Учетной записи с таким именем ' \
                                    'пользователя нет в базе данных'
    else:
        form = UserLoginForm(data=request.POST)

    context = {
        'page_title': title_login + title_for_basic_template(),
        'message_error': message_error,
        'form': form
    }
    return render(request, 'login.html', context)


def register(request):
    title_register: str = 'Регистрация - '

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
        'page_title': title_register + title_for_basic_template(),
        'form': form
    }
    return render(request, 'register.html', context)


def email_verification(request, email, code):
    title_register: str = 'Подтверждение адреса электронной почты - '

    user = User.objects.get(email=email)
    for_email_verification = \
        EmailVerification.objects.filter(user=user,
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


def forgot_password(request):
    title_register: str = 'Востановление пароля - '
    message_error: str = ''
    message_success: str = ''

    if request.method == 'POST':
        form = UserRecoveryPasswordForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists() \
                    and User.objects.get(email=email).is_verified_email:
                user = User.objects.get(email=email)
                expiration = now() + timedelta(hours=48)
                record = PasswordRecovery.objects.create(code=uuid.uuid4(),
                                                         user=user,
                                                         expiration=expiration)
                record.send_password_recovery_email()
                message_success = f"На электронную почту {email} " \
                                  f"отправлено письмо содержащее " \
                                  f"ссылку для востановления пароля."

            else:
                message_error = f"Учетной записи с таким адресом " \
                                f"электронной почты не существует " \
                                f"или электроная почта не подтверждена."
    else:
        form = UserRecoveryPasswordForm()

    context = {
        'page_title': title_register + title_for_basic_template(),
        'message_success': message_success,
        'message_error': message_error,
        'form': form
    }
    return render(request, 'forgot_password.html', context)


def create_new_password(request, email, code):
    title_register: str \
        ='Создание нового пароля взамен забытого - '

    user = User.objects.get(email=email)
    application_for_new_password = \
        PasswordRecovery.objects.filter(user=user,
                                        code=code)

    if application_for_new_password.exists() and \
            not application_for_new_password.first().is_expired():
        if request.method == 'POST':
            form = UserCreatNewPasswordForm(data=request.POST)
            if form.is_valid():
                #form.save()
                new_password = form.cleaned_data['password2']
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Ваш пароль изминен !')
                return HttpResponseRedirect(reverse('users:login'))
        else:
            form = UserCreatNewPasswordForm()
    else:
        return HttpResponseRedirect(reverse('index'))

    context = {
        'page_title': title_register + title_for_basic_template(),
        'form': form,
        'email': email,
        'code': code
    }
    return render(request, 'new_password.html', context)


@login_required
def my_account(request):
    title_my_account: str = 'Личный кабинет - '

    if request.method == 'POST':
        form = UserProfileForm(instance=request.user,
                               data=request.POST,
                               files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:my_account'))
    else:
        form = UserProfileForm(instance=request.user)

    context = {
        'form': form,
        'page_title': title_my_account + title_for_basic_template(),
    }
    return render(request, 'my_account.html',
                  {**context, **data_for_basic_template(request)})


@login_required
def delete_profile(request):
    username = request.POST["username"]
    if User.objects.filter(username=username).exists():
        auth.logout(request)
        User.objects.filter(username=username).delete()
        return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def exit_my_account(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
