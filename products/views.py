from django.shortcuts import render
from .models import Product

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

    # Pass the search query to the template
    context = {
        'products': products,
        'categories': categories,
        'search_query': search_query
    }
    return render(request, 'all_products.html', context)
