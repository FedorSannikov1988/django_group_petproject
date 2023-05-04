from django.template.response import TemplateResponse
from django.shortcuts import render


title = 'Дипломный проект студентов GB'


def index(request):

    title_index = 'Главная страница - '

    context = {
        'page_title': title_index + title,
    }
    return render(request, 'index.html', context)


def sitemap(request):

    title_sitemap = 'Карта сайта - '

    context = {
        'page_title': title_sitemap + title,
    }
    return render(request, 'sitemap.html', context)


def about_us(request):

    title_about_us = 'О нас/Наши контакты - '

    context = {
        'page_title': title_about_us + title,
    }
    return render(request, 'about_us.html', context)


def faq(request):

    title_faq = 'Полезная информация - '

    context = {
        'page_title': title_faq + title,
    }
    return render(request, 'faq.html', context)


def cart(request):

    title_cart = 'Корзина покупателя - '

    context = {
        'page_title': title_cart + title,
    }
    return render(request, 'cart.html', context)


def login(request):

    title_login = 'Вход в учетную запись - '

    context = {
        'page_title': title_login + title,
    }

    return render(request, 'login.html', context)


def register(request):

    title_register = 'Регистрация - '

    context = {
        'page_title': title_register + title,
    }
    return render(request, 'register.html', context)
