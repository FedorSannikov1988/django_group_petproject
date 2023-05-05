from django.urls import path, re_path

from shop.views import faq
from shop.views import sitemap
from shop.views import about_us

app_name = 'faq'

urlpatterns = [
    path('', faq, name='index'),
]