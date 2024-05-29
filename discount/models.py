from django.db import models
from checkout.models import Order

class DiscountCode(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)  # Discount as a percentage
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code

class AppliedDiscount(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='applied_discount')
    discount_code = models.ForeignKey(DiscountCode, on_delete=models.SET_NULL, null=True, blank=True)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Discount {self.discount_code} applied to order {self.order.order_number}"
