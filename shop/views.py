from django.template.response import TemplateResponse
from django.shortcuts import render

from shop.models import SoftwareCategory, Software, DevelopmentTeam, FAQ

# глобальные переменные/данные:

title_for_basic_template = 'Дипломный проект студентов GB'

data_for_basic_template = {
    "software_category": SoftwareCategory.objects.all(),
    "software_operating_systems": Software.objects.filter(category__name='Операционные системы'),
    "software_office": Software.objects.filter(category__name='Офисное ПО'),
    "software_antivirus_protection": Software.objects.filter(category__name='Антивирусная защита')
}


def index(request):

    title_index = 'Главная страница - '

    context = {
        'page_title': title_index + title_for_basic_template,
        "all_soft": Software.objects.all(),
    }
    return render(request, 'index.html', {**context, **data_for_basic_template})


def sitemap(request):

    title_sitemap = 'Карта сайта - '

    context = {
        'page_title': title_sitemap + title_for_basic_template,
    }
    return render(request, 'sitemap.html', {**context, **data_for_basic_template})


def about_us(request):

    title_about_us = 'О нас / Наши контакты - '

    context = {
        "page_title": title_about_us + title_for_basic_template,
        "development_team": DevelopmentTeam.objects.all(),
    }
    return render(request, 'about_us.html', {**context, **data_for_basic_template})


def faq(request):

    title_faq = 'Полезная информация - '

    context = {
        'page_title': title_faq + title_for_basic_template,
        'faq': FAQ.objects.all(),
    }
    return render(request, 'faq.html', {**context, **data_for_basic_template})


def cart(request):

    title_cart = 'Корзина покупателя - '

    context = {
        'page_title': title_cart + title_for_basic_template,
    }
    return render(request, 'cart.html', {**context, **data_for_basic_template})

def product(request):

    title_product = 'Описание продукта - '

    context = {
        'page_title': title_product + title_for_basic_template,
    }

    return render(request, 'product.html', {**context, **data_for_basic_template})
