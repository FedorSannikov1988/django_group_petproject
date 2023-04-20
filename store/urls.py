from django.contrib import admin

from django.urls import path, re_path


from shop.views import index
from shop.views import sitemap
from shop.views import about_us
from shop.views import login
from shop.views import register

urlpatterns = [
    path("", index, name='index'),
    path("sitemap", sitemap, name='sitemap'),
    path("about_us", about_us, name='about_us'),
    path("login", login, name='login'),
    path("register", register, name='register'),
]
