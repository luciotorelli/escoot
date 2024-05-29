# discount/views.py
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from .models import DiscountCode, AppliedDiscount
from .forms import DiscountCodeApplyForm
from checkout.models import Order

def apply_discount(request):
    form = DiscountCodeApplyForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            code = form.cleaned_data['code']
            try:
                discount_code = DiscountCode.objects.get(code=code, active=True, valid_from__lte=timezone.now(), valid_to__gte=timezone.now())
                order = Order.objects.get(user_profile=request.user.userprofile, status='Pending')  # Assuming you have a way to get the current order
                discount_amount = (discount_code.discount / 100) * order.grand_total
                applied_discount, created = AppliedDiscount.objects.update_or_create(
                    order=order,
                    defaults={'discount_code': discount_code, 'discount_amount': discount_amount}
                )
                order.grand_total -= discount_amount
                order.save()
                messages.success(request, f'Discount code {code} applied successfully!')
                return redirect('checkout:summary')  # Redirect to your order summary page
            except DiscountCode.DoesNotExist:
                messages.error(request, 'This discount code is invalid or expired.')
    return render(request, 'discount/apply_discount.html', {'form': form})
