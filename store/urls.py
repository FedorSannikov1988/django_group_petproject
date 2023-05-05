from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings

from shop.views import index
from shop.views import sitemap
from shop.views import about_us
from shop.views import login
from shop.views import register
from shop.views import cart
from shop.views import faq

from django.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name='index'),
    path("sitemap", sitemap, name='sitemap'),
    path("about_us", about_us, name='about_us'),
    path("login", login, name='login'),
    path("register", register, name='register'),
    path("cart", cart, name='cart'),
    #path('faq', faq, name='faq'),
    path('faq', include('faq.urls', namespace='faq')),
    #path('faq', include('faq.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
