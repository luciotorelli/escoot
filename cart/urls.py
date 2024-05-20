# cart/urls.py
from django.urls import path
from .views import cart, add_to_cart, adjust_cart, remove_from_cart

app_name = 'cart'

urlpatterns = [
    path('', cart, name='cart'),
    path('add/<item_id>/', add_to_cart, name='add_to_cart'),
    path('adjust_cart/<item_id>/', adjust_cart, name='adjust_cart'),
    path('remove_from_cart/<item_id>/', remove_from_cart, name='remove_from_cart'),        
]