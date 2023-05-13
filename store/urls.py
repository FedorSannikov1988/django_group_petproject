from django.contrib import admin

from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static
from shop.views import index, sitemap, about_us, cart, product, faq

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name='index'),
    path("sitemap", sitemap, name='sitemap'),
    path("about_us", about_us, name='about_us'),
    path("product", product, name='product'),
    path("cart", cart, name='cart'),
    path("faq", faq, name='faq'),
    path("input_user/", include('users.urls', namespace='users')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
