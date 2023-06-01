from django.urls import path
from shop.views import products_catalog, cart_add_one, cart_delete_one, cart_remove

app_name = 'products_catalog'

urlpatterns = [
    path('', products_catalog, name='index'),
    path('category/<int:category_id>/', products_catalog, name='category'),
    path('page/<int:page_number>/', products_catalog, name='paginator'),
    path('cart/add/<int:software_id>/', cart_add_one, name='cart_add_one'),
    path('cart/delete/<int:software_id>/', cart_delete_one, name='cart_delete_one'),
    path('cart/remove/<int:cart_id>/', cart_remove, name='cart_remove'),
]