from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import DiscountCode
from .forms import DiscountCodeForm

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

@login_required
def discount_list(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    discounts = DiscountCode.objects.all()
    
    if request.method == 'POST':
        if 'create_discount' in request.POST:
            create_form = DiscountCodeForm(request.POST)
            if create_form.is_valid():
                create_form.save()
                messages.success(request, 'Discount code created successfully.')
                return redirect('discount:discount_list')
            else:
                messages.error(request, 'Error creating discount code. Please check the form.')
        elif 'update_discount' in request.POST:
            pk = request.POST.get('id')
            discount = get_object_or_404(DiscountCode, pk=pk)
            edit_form = DiscountCodeForm(request.POST, instance=discount)
            if edit_form.is_valid():
                edit_form.save()
                messages.success(request, 'Discount code updated successfully.')
                return redirect('discount:discount_list')
            else:
                messages.error(request, 'Error updating discount code. Please check the form.')
        elif 'delete_discount' in request.POST:
            pk = request.POST.get('id')
            discount = get_object_or_404(DiscountCode, pk=pk)
            discount.delete()
            messages.success(request, 'Discount code deleted successfully.')
            return redirect('discount:discount_list')
    
    create_form = DiscountCodeForm()
    edit_form = DiscountCodeForm()
    return render(request, 'discount/discount_list.html', {
        'discounts': discounts,
        'create_form': create_form,
        'edit_form': edit_form
    })

