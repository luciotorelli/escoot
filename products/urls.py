# products/urls.py
from django.urls import path
from .views import *

app_name = 'products'

urlpatterns = [
    path('all/', all_products, name='all_products'),
    path('escooter-builder/', escooter_builder, name='escooter_builder'),
    path('add/', add_product, name='add_product'),    
    path('edit/<int:product_id>/', edit_product, name='edit_product'),
    path('delete/<int:product_id>/', delete_product, name='delete_product'),
]
