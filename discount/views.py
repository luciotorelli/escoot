from django.http import JsonResponse
from .models import DiscountCode

def validate_discount_code(request):
    code = request.GET.get('code', '')
    try:
        discount_code = DiscountCode.objects.get(code=code, active=True)
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
