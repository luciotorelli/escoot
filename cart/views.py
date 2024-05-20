from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from products.models import Product

def cart(request):
    """ A view to return the index page """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in cart:
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart

    messages.success(request, f'You have added {product.product_name} to your bag.')

    return redirect(redirect_url)

def adjust_cart(request, item_id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('cart:cart'))

def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})

    cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('cart:cart'))