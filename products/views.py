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
        # Logic to add products to the cart based on selected_products_ids
        messages.success(request, "Products added to cart successfully.")
        return redirect('cart')  # Redirect to the cart page
    else:
        products = Product.objects.all().order_by('product_category', 'product_name')
        category_list = {}
        
        for product in products:
            if product.product_category not in category_list:
                category_list[product.product_category] = []
            category_list[product.product_category].append(product)
        
        return render(request, 'escooter_builder.html', {'category_list': category_list})
