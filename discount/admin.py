from django.contrib import admin
from .models import DiscountCode, AppliedDiscount

@admin.register(DiscountCode)
class DiscountCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'discount', 'active']
    list_filter = ['active']
    search_fields = ['code']

@admin.register(AppliedDiscount)
class AppliedDiscountAdmin(admin.ModelAdmin):
    list_display = ['order', 'discount_code', 'discount_amount']
    search_fields = ['order__order_number', 'discount_code__code']
