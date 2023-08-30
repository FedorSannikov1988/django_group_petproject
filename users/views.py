from uuid import uuid4
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from django.shortcuts import render, \
    HttpResponseRedirect
from django.contrib.auth import authenticate, \
    login, \
    logout
from django.urls import reverse
from django.contrib.messages import success, \
    error
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
from django.conf import settings

QUANTITY_LIMIT_EMAIL_DAY: int = 5
email_confirmation_time_hours = \
    settings.EMAIL_CONFIRMATION_TIME_HOURS
password_recovery_time_hours = \
    settings.PASSWORD_RECOVERY_TIME_HOURS


def login_user(request):
    """
    Displays the login page for the personal account
    and processes the user authentication form.

    :return: Redirection to the user's personal account page
    in case of successful authentication.
    Otherwise, display the login page with the form.
    """
    title_login: str = 'Вход в личный кабинет - '

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username,
                                password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('users:my_account'))
            else:
                message_error_for_user: str = ''
                if User.objects.filter(username=username).exists():
                    message_error_for_user = 'Неверный пароль'
                else:
                    message_error_for_user = 'Учетной записи с таким именем ' \
                                             'пользователя нет в базе данных'
                error(request, message_error_for_user)
    else:
        form = UserLoginForm(data=request.POST)

    context = {
        'form': form,
        'page_title': title_login + title_for_basic_template(),
    }
    return render(request, 'login.html', context)


def register(request):
    """
    Processes the form to create a new user account.
    Saves the user in the database by filling the username field with the data
    from the email field.

    :return: Redirecting to the login page in case of successful registration.
    Otherwise, displaying the registration page with the form
    """
    title_register: str = 'Регистрация покупателя - '

    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            username_form = form.save(commit=False)
            username_form.username = form.cleaned_data['email']
            username_form.save()

            expiration = now() + timedelta(hours=
                                           settings.EMAIL_CONFIRMATION_TIME_HOURS)
            new_user = User.objects.get(username=
                                        username_form.username)
            confirmation_email = \
                EmailVerification.objects.create(user=new_user,
                                                 code=uuid4(),
                                                 expiration=expiration)
            confirmation_email.send_verification_email()
            message_success_for_user: str = \
                'Вы успешно прошли регистрацию!'
            success(request, message_success_for_user)
            return HttpResponseRedirect(reverse('users:login_user'))
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
        'page_title': title_register + title_for_basic_template()
    }
    return render(request, 'register.html', context)


def email_verification(request, email, code):
    title_register: str = \
        'Подтверждение адреса электронной почты - '

    if User.objects.filter(email=email).exists():
        user = User.objects.get(email=email)
        for_email_verification = \
            EmailVerification.objects.filter(user=user,
                                             code=code)
        if for_email_verification.exists() and \
                not for_email_verification.first().is_expired():
            user.is_verified_email = True
            user.save()
            message_success_for_user: str = \
                f'Вы успешно подвердили ' \
                f'адрес электронной почты: ' \
                f'{email}'
            success(request, message_success_for_user)

        elif for_email_verification.exists() and \
                for_email_verification.first().is_expired():
            message_error_for_user: str = \
                f'Время длительностью в ' \
                f'{email_confirmation_time_hours} ' \
                f'часов отведенное на подтверждение ' \
                f'адреса электронной почты вышло.' \
                f'Обратитесь к администрации ' \
                f'ресурса .'
            error(request, message_error_for_user)

        elif not for_email_verification.exists():
            message_error_for_user = \
                f'Письмо с данной ссылкой некогда ' \
                f'не отправлялось ' \
                f'на электронную почту {email} .'
            error(request, message_error_for_user)
    else:
        message_error_for_user = 'Такого пользователя ' \
                                 'не существует.'
        error(request, message_error_for_user)

    context = {
        'page_title': title_register + title_for_basic_template()
    }
    return render(request, 'email_verification.html', context)


def forgot_password(request):
    title_register: str = 'Востановление пароля - '

    if request.method == 'POST':
        form = UserRecoveryPasswordForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.filter(email=email)

            if user.exists() and \
                    user.first().is_verified_email:

                end_date = now()
                start_date = end_date - timedelta(hours=24)
                count_emails = \
                    PasswordRecovery.objects.filter(user=user.first(),
                                                    created__range=
                                                    (start_date, end_date)).count()

                if count_emails <= QUANTITY_LIMIT_EMAIL_DAY:
                    expiration = now() + timedelta(hours=
                                                   password_recovery_time_hours)
                    for_password_recovery = \
                        PasswordRecovery.objects.create(code=uuid4(),
                                                        user=user.first(),
                                                        expiration=expiration)

                    for_password_recovery.send_password_recovery_email()

                    message_success_for_user: str = \
                        f"На электронную почту {email} " \
                        f"отправлено письмо содержащее " \
                        f"ссылку для востановления пароля."
                    success(request, message_success_for_user)
                else:
                    message_error_for_user: str = \
                        f"В сутки можно отправить " \
                        f"{QUANTITY_LIMIT_EMAIL_DAY} " \
                        f"писем. "
                    error(request, message_error_for_user)
            else:
                message_error_for_user: str = \
                    f"Учетной записи с таким адресом " \
                    f"электронной почты не существует " \
                    f"или электроная почта не подтверждена."
                error(request, message_error_for_user)
    else:
        form = UserRecoveryPasswordForm()

    context = {
        'form': form,
        'page_title': title_register + title_for_basic_template()
    }
    return render(request, 'forgot_password.html', context)


def create_new_password(request, email, code):
    title_register: str = \
        'Создание нового пароля взамен забытого - '

    if User.objects.filter(email=email).exists():
        user = User.objects.get(email=email)
        application_for_new_password = \
            PasswordRecovery.objects.filter(user=user,
                                            code=code)

        if application_for_new_password.exists() and \
                not application_for_new_password.first().is_expired() and \
                not application_for_new_password.first().link_used:

            if request.method == 'POST':
                form = UserCreatNewPasswordForm(data=request.POST)
                if form.is_valid():
                    new_password = form.cleaned_data['password2']
                    user.set_password(new_password)
                    user.save()

                    for_neutralize_link = \
                        application_for_new_password.first()
                    for_neutralize_link.link_used = True
                    for_neutralize_link.save()

                    message_success_for_user: str = \
                        "Ваш пароль был изминен !"
                    success(request, message_success_for_user)
                    return HttpResponseRedirect(reverse('users:login_user'))

        elif application_for_new_password.exists() and \
                not application_for_new_password.first().is_expired() and \
                application_for_new_password.first().link_used:

            message_error_for_user: str = \
                'Эта ссылка уже использована один раз.' \
                'Повторное использование невозможно .'
            error(request, message_error_for_user)

        elif application_for_new_password.exists() and \
                application_for_new_password.first().is_expired() and \
                not application_for_new_password.first().link_used:

            message_error_for_user: str = \
                f'Время длительностью в ' \
                f'{password_recovery_time_hours} ' \
                f'часов отведенное на восстановления ' \
                f'пароля по присланной ссылке ' \
                f'на почту {email} вышло.'
            error(request, message_error_for_user)

        elif not application_for_new_password.exists():
            message_error_for_user = \
                f'Письмо c ссылкой ' \
                f'для востановления ' \
                f'пароля не отправлялось ' \
                f'на электронную почту {email} .'
            error(request, message_error_for_user)

    else:
        message_error_for_user = \
            'Такого пользователя не существует.'
        error(request, message_error_for_user)

    form = UserCreatNewPasswordForm()

    context = {
        'form': form,
        'email': email,
        'code': code,
        'page_title': title_register + title_for_basic_template()
    }
    return render(request, 'new_password.html', context)


@login_required
def my_account(request):
    """
    Displays the user's personal account page and processes the form
    to save changes to the user's profile.


    :return: Redirection to the user's personal account page
    in case of successful saving of profile changes. Otherwise,
    redirect to the current page.
    """
    title_my_account: str = 'Личный кабинет пользователя - '

    if request.method == 'POST':
        form = UserProfileForm(instance=request.user,
                               data=request.POST,
                               files=request.FILES)

        if (not request.user.is_superuser) or \
                (not request.user.is_staff):
            form = UserProfileForm(instance=request.user,
                                   data={
                                       'username': form.data['email'],
                                       'first_name': form.data['first_name'],
                                       'last_name': form.data['last_name'],
                                       'surname': form.data['surname'],
                                       'email': form.data['email'],
                                       'phone': form.data['phone'],
                                       'birthday': form.data['birthday'],
                                       'address': form.data['address'],
                                       'gender': form.data['gender']},
                                   files=request.FILES)
        if form.is_valid():
            form.save()
            message_success_for_user: str = \
                "Изминения сохранены"
            success(request, message_success_for_user)
        else:
            message_error_for_user = \
                "Внимание изминения не могут быть сохранены !"

            if User.objects.filter(phone=form.data['phone']).exists():
                message_error_for_user += " " \
                                          "Пользователь с таким номером " \
                                          "телефона уже существует в " \
                                          "базе данных !"
            error(request, message_error_for_user)
        return HttpResponseRedirect(reverse('users:my_account'))

    form = UserProfileForm(instance=request.user)

    context = {
        'form': form,
        'page_title': title_my_account + title_for_basic_template(),
    }
    return render(request, 'my_account.html',
                  {**context, **data_for_basic_template(request)})


@login_required
def delete_user_confirmation(request):
    """
    Displays the user account deletion confirmation page.

    :return: display of the template `delete_user_confirmation.html` with context.
    """
    title_index = \
        'Подтверждение удаления ' \
        'учетной записи пользователя - '

    context = {
        "page_title": title_index + title_for_basic_template()
    }
    return render(request, 'delete_user_confirmation.html', context)


@login_required
def delete_profile(request):
    """
    The function takes username. If a user with that username exists,
    then the user's profile is removed from the database.
    If the user does not exist, then redirect to the previous page

    :return: display of the template `index.html` with context.
    """
    username: str = request.user.username
    if User.objects.filter(username=username).exists():
        User.objects.get(username=username).delete()
        logout(request)
        return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def exit_my_account(request):
    """
    Logs out of the user account.

    :return: display of the template `index.html` with context.
    """
    logout(request)
    return HttpResponseRedirect(reverse('index'))
