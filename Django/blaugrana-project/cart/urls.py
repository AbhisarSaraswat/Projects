from django.urls import path, include
from django.urls import re_path
from . import views


# Cart Urls
urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>',views.add_to_cart, name='add_to_cart'),
    path('remove/<product_id>', views.remove_cart, name='remove_cart'),
]