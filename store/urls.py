from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings

from shop.views import index
from shop.views import sitemap
from shop.views import about_us

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name='index'),
    path("sitemap", sitemap, name='sitemap'),
    path("about_us", about_us, name='about_us'),
] #+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)