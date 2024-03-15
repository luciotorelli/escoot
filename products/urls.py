# products/urls.py
from django.urls import path
from .views import all_products

app_name = 'products'

urlpatterns = [
    path('all/', all_products, name='all_products'),
]
