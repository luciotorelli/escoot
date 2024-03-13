from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock_quantity', 'status', 'product_category')
    search_fields = ('product_name',)
