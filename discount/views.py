# discount/views.py
from django.http import JsonResponse
from django.utils import timezone
from .models import DiscountCode

def validate_discount_code(request):
    code = request.GET.get('code', '')
    try:
        discount_code = DiscountCode.objects.get(code=code, active=True, valid_from__lte=timezone.now(), valid_to__gte=timezone.now())
        response = {
            'valid': True,
            'discount': discount_code.discount,
        }
    except DiscountCode.DoesNotExist:
        response = {
            'valid': False,
            'error': 'This discount code is invalid or expired.'
        }
    return JsonResponse(response)
