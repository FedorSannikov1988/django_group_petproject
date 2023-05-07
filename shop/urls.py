from django.urls import path

from shop.views import faq

app_name = 'faq'

urlpatterns = [
    path('', faq, name='index'),
]