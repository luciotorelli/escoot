# cart/context.py

from django.conf import settings

def cart_contents(request):
    cart_items = []
    total = 0 
    product_count = 0 

    # Delivery cost
    delivery_threshold = settings.FREE_DELIVERY_THRESHOLD
    standard_delivery_percentage = settings.STANDARD_DELIVERY_PERCENTAGE
    free_delivery_delta = 0
    delivery = 0
    grand_total = 0

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': delivery_threshold,
        'grand_total': grand_total,
    }
    return context
