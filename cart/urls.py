# cart/urls.py
from django.urls import path
from .views import cart, add_to_cart

app_name = 'cart'

urlpatterns = [
    path('', cart, name='cart'),
    path('add/<item_id>/', add_to_cart, name='add_to_cart'),    
]