from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from products.models import Product
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.http import HttpResponse

def cart(request):
    """ A view to return the cart page """
    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ 
    A view to add a product to the cart.
    Shows a success message with a link to the cart page.
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in cart:
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart

    cart_url = reverse('cart:cart')
    messages.success(request, mark_safe(f'You have added {escape(product.product_name)} to your <a href="{cart_url}">Cart</a>.'))

    return redirect(redirect_url)

def adjust_cart(request, item_id):
    """ 
    A view to adjust the quantity of a product in the cart.
    Shows a success message with a link to the cart page when the quantity is updated.
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        if item_id in cart:
            old_quantity = cart[item_id]
            cart[item_id] = quantity
            if old_quantity != cart[item_id]:
                cart_url = reverse('cart:cart')
                messages.success(request, mark_safe(f'Updated {escape(product.product_name)} quantity to {cart[item_id]} in your <a href="{cart_url}">Cart</a>'))
    else:
        if item_id in cart:
            cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('cart:cart'))

def remove_from_cart(request, item_id):
    """ 
    A view to remove a product from the cart.
    Shows a success message with a link to the cart page when a product is removed.
    """
    product = get_object_or_404(Product, pk=item_id)
    cart = request.session.get('cart', {})

    try:
        if item_id in cart:
            cart.pop(item_id)
            cart_url = reverse('cart:cart')
            messages.success(request, mark_safe(f'Removed {escape(product.product_name)} from your <a href="{cart_url}">Cart</a>'))
            request.session['cart'] = cart
            return redirect(reverse('cart:cart'))
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)