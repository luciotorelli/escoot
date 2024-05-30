from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from discount.models import DiscountCode

def cart_contents(request):
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {}).copy()
    discount_code = request.session.get('discount_code', None)
    discount_amount = Decimal('0.00')

    for item_id, quantity in list(cart.items()):
        try:
            product = get_object_or_404(Product, pk=item_id)
            total += quantity * product.price
            product_count += quantity
            cart_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
            })
        except Product.DoesNotExist:
            del cart[item_id]
            request.session['cart'] = cart

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    if discount_code:
        try:
            discount = DiscountCode.objects.get(code=discount_code, active=True)
            discount_amount = (discount.discount / Decimal('100')) * total
            grand_total -= discount_amount
        except DiscountCode.DoesNotExist:
            request.session['discount_code'] = None

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'discount_amount': discount_amount,
        'grand_total': grand_total,
        'applied_discount_code': discount_code,
    }

    return context
