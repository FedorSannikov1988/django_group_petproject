from django.contrib import admin

from django.urls import path, re_path


from shop.views import index
from shop.views import sitemap
from shop.views import about_us

urlpatterns = [
    path("", index, name='index'),
    path("sitemap", sitemap, name='sitemap'),
    path("about_us", about_us, name='about_us'),
]
