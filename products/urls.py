# products/urls.py
from django.urls import path
from .views import all_products, escooter_builder, add_product

app_name = 'products'

urlpatterns = [
    path('all/', all_products, name='all_products'),
    path('escooter-builder/', escooter_builder, name='escooter_builder'),
    path('add/', add_product, name='add_product'),    
]
