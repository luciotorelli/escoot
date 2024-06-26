from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm
from django.contrib import messages
from django.urls import reverse
from django.db import IntegrityError
from wishlist.models import Wishlist


def all_products(request):
    """
    Render all products with optional sorting, filtering, and search.

    Args:
        request: HttpRequest object containing sorting, filtering, and search parameters.

    Returns:
        Rendered template with sorted, filtered, and searched product data.
    """
    # Retrieve sorting, filtering, and search parameters from the request
    sort_by = request.GET.get('sort_by')
    category_filter = request.GET.get('category')
    search_query = request.GET.get('search')

    # Get all products queryset
    products = Product.objects.all()

    # Apply filtering if category is selected
    if category_filter:
        products = products.filter(product_category=category_filter)

    # Apply search filtering if query is present
    if search_query:
        products = products.filter(product_name__icontains=search_query)

    # Apply sorting based on the selected criteria
    if sort_by == 'price_low_to_high':
        products = products.order_by('price')
    elif sort_by == 'price_high_to_low':
        products = products.order_by('-price')

    # Get unique categories
    categories = Product.objects.values_list('product_category', flat=True).distinct()

    wishlist_product_ids = []
    if request.user.is_authenticated:
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        wishlist_product_ids = wishlist.products.values_list('product_id', flat=True)

    # Pass the search query to the template
    context = {
        'products': products,
        'categories': categories,
        'search_query': search_query,
        'wishlist_product_ids': wishlist_product_ids,
    }
    return render(request, 'all_products.html', context)

def escooter_builder(request):
    """
    Render the e-scooter builder page allowing users to select products to build their e-scooter.

    If the request method is POST, process the selected products and add them to the cart.
    If the request method is GET, retrieve all products and organize them by category for display.

    Args:
        request: HttpRequest object containing the HTTP request data.

    Returns:
        Rendered template with e-scooter builder page, displaying products organized by category.
    """
    if request.method == 'POST':
        selected_products_ids = request.POST.getlist('selected_products')
        # Filter out empty values
        selected_products_ids = [pid for pid in selected_products_ids if pid]
        quantity = 1  # Default quantity for builder products
        cart = request.session.get('cart', {})

        for product_id in selected_products_ids:
            product = get_object_or_404(Product, pk=product_id)
            if product_id in cart:
                cart[product_id] += quantity
            else:
                cart[product_id] = quantity

        request.session['cart'] = cart
        messages.success(request, "Products added to cart successfully.")
        return redirect('cart:cart')
    else:
        products = Product.objects.all().order_by('product_category', 'product_name')
        category_list = {}
        
        for product in products:
            if product.product_category not in category_list:
                category_list[product.product_category] = []
            category_list[product.product_category].append(product)
        
        return render(request, 'escooter_builder.html', {'category_list': category_list})

@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('products:add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            referer = request.META.get('HTTP_REFERER', '/')
            return redirect(referer)
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.product_name}')

    template = 'edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products:all_products'))