from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from shop.views import index, sitemap, about_us, product, cart, faq, search_product

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name='index'),
    path("sitemap", sitemap, name='sitemap'),
    path("about_us", about_us, name='about_us'),
    path("product", product, name='product'),
    path("cart", cart, name='cart'),
    path("faq", faq, name='faq'),
    path("input_user/", include('users.urls', namespace='users')),
    path("products_catalog/", include('shop.urls', namespace='products_catalog')),
    path("product/", include('shop.urls', namespace='product')),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
    path("search", search_product, name='search'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)