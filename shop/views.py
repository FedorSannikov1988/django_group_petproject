from django.template.response import TemplateResponse
from django.shortcuts import render

from shop.models import SoftwareCategory, Software, FeaturesSoftware, DevelopmentTeam


def index(request):
    context = {
    "all_soft": Software.objects.all(),
    "software_category": SoftwareCategory.objects.all(),
    "software_operating_systems": Software.objects.filter(category__name='Операционные системы'),
    "software_office": Software.objects.filter(category__name='Офисное ПО'),
    "software_antivirus_protection": Software.objects.filter(category__name='Антивирусная защита')
    }
    return render(request, 'index.html', context)


def sitemap(request):
    context = {
    "software_category": SoftwareCategory.objects.all(),
    "software_operating_systems": Software.objects.filter(category__name='Операционные системы'),
    "software_office": Software.objects.filter(category__name='Офисное ПО'),
    "software_antivirus_protection": Software.objects.filter(category__name='Антивирусная защита')
    }
    return render(request, 'sitemap.html', context)


def about_us(request):
    context = {
    "development_team": DevelopmentTeam.objects.all()
    }
    return render(request, 'about_us.html', context)
