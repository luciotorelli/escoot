from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.views.generic import TemplateView
from .views import handler404

from escoot.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', include('home.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),  
    path('checkout/', include('checkout.urls')),  
    path('profile/', include('profiles.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('contact/', include('contact.urls')),
    path('discount/', include('discount.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]

handler404 = 'escoot.views.handler404'
