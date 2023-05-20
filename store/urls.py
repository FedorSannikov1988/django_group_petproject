from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from shop.views import index, sitemap, about_us, cart, product, faq, catalog


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name='index'),
    path("sitemap", sitemap, name='sitemap'),
    path("about_us", about_us, name='about_us'),
    path("product", product, name='product'),
    path("cart", cart, name='cart'),
    path("catalog/", catalog, name='catalog'),
    path("faq", faq, name='faq'),
    path("input_user/", include('users.urls', namespace='users')),
    path("product_catalog/", include('shop.urls', namespace='product_catalog')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)