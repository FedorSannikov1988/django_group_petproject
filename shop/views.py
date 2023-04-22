from django.template.response import TemplateResponse
from django.shortcuts import render

title = 'Дипломный проект - Интернет магазин программного обеспечения'
def index(request):
    context = {
        'title_base': title,
    }
    return render(request, 'index.html', context)

def sitemap(request):
    title_sitemap = 'Карта сайта - '
    context = {
        'title_base': title_sitemap + title,
    }
    return render(request, 'sitemap.html', context)

def about_us(request):
    title_about_us = 'О нас - '
    context = {
        'title_base': title_about_us + title,
    }
    return render(request, 'about_us.html',context)

def faq(request):
    title_faq = 'Полезная информация - '
    context = {
        'title_base': title_faq + title,
    }
    return render(request, 'faq.html', context)