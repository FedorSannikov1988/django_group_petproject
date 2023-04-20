from django.template.response import TemplateResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def sitemap(request):
    return render(request, 'sitemap.html')


def about_us(request):
    return render(request, 'about_us.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')
