from django.template.response import TemplateResponse
from django.shortcuts import render

from shop.models import SoftwareCategory, SoftwareSubcategories, Software, FeaturesSoftware

def index(request):
    context = {
    "all_soft": Software.objects.all(),
    "software_category": SoftwareCategory.objects.all(),
    "software_subcategories_operating_systems": SoftwareSubcategories.objects.all().filter(category__name='Операционные системы'),
    "software_subcategories_office_software": SoftwareSubcategories.objects.all().filter(category__name='Офисное ПО'),
    "software_subcategories_antivirus_protection": SoftwareSubcategories.objects.all().filter(category__name='Антивирусная защита'),
    "software_operating_systems": Software.objects.all().filter(subcategories__name='Windows'),
    }
    return render(request, 'index.html', context)

def sitemap(request):
    context = {
    "software_category": SoftwareCategory.objects.all(),
    "software_subcategories_operating_systems": SoftwareSubcategories.objects.all().filter(category__name='Операционные системы'),
    "software_subcategories_office_software": SoftwareSubcategories.objects.all().filter(category__name='Офисное ПО'),
    "software_subcategories_antivirus_protection": SoftwareSubcategories.objects.all().filter(category__name='Антивирусная защита'),
    "software_operating_systems": Software.objects.all().filter(subcategories__name='Windows'),
    }
    return render(request, 'sitemap.html', context)

def about_us(request):
    return render(request, 'about_us.html')