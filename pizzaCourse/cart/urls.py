from django.urls import path

from .views import add_to_cart, remove_from_cart, get_cart, plus_1, minus_1, order

urlpatterns = [
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>', remove_from_cart, name='remove_from_cart'),
    path('', get_cart, name='get_cart'),
    path('plus_one/<int:product_id>/<int:quantity>/', plus_1, name='plus_1'),
    path('minus_one/<int:product_id>/<int:quantity>/', minus_1, name='minus_1'),
    path('order/', order, name='order'),
]
