from django.template.response import TemplateResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def sitemap(request):
    return render(request, 'sitemap.html')

def about_us(request):
    return render(request, 'about_us.html')