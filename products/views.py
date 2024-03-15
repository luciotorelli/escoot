from django.shortcuts import render
from .models import Product

def all_products(request):
    """
    Render all products with optional sorting and filtering.

    Args:
        request: HttpRequest object containing sorting and filtering parameters.

    Returns:
        Rendered template with sorted and filtered product data.
    """
    # Retrieve sorting and filtering parameters from the request
    sort_by = request.GET.get('sort_by')
    category_filter = request.GET.get('category')

    # Get all products queryset
    products = Product.objects.all()

    # Apply filtering if category is selected
    if category_filter:
        products = products.filter(product_category=category_filter)

    # Apply sorting based on the selected criteria
    if sort_by == 'price_low_to_high':
        products = products.order_by('price')
    elif sort_by == 'price_high_to_low':
        products = products.order_by('-price')

    # Get unique categories
    categories = Product.objects.values_list('product_category', flat=True).distinct()

    return render(request, 'all_products.html', {'products': products, 'categories': categories})
