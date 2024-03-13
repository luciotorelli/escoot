# products/views.py
from django.shortcuts import render
from .models import Product

def all_products(request):
    products = Product.objects.all()
    return render(request, 'all_products.html', {'products': products})
