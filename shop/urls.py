from django.urls import path

from shop.views import product_catalog, cart_add, cart_remove

app_name = 'product_catalog'

urlpatterns = [
    path('', product_catalog, name='index'),
    path('cart/add/<int:software_id>/', cart_add, name='cart_add'),
    path('cart/remove/<int:cart_id>/', cart_remove, name='cart_remove'),
]