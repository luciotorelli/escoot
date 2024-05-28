from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Wishlist
from products.models import Product

@login_required
def wishlist_view(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    return render(request, 'wishlist/wishlist.html', {'wishlist': wishlist})

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    if wishlist.products.filter(product_id=product_id).exists():
        messages.info(request, 'This product is already in your wishlist.')
    else:
        wishlist.products.add(product)
        messages.success(request, 'Product added to your wishlist.')
    return redirect('wishlist:wishlist_view')

@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    wishlist = get_object_or_404(Wishlist, user=request.user)
    if wishlist.products.filter(product_id=product_id).exists():
        wishlist.products.remove(product)
        messages.success(request, 'Product removed from your wishlist.')
    else:
        messages.error(request, 'Product not found in your wishlist.')
    return redirect('wishlist:wishlist_view')
