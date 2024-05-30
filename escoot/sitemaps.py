from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        # Add the view names you specified
        return [
            'home',  # from home app
            'products:all_products',  # from products app
            'products:escooter_builder',  # from products app
            'cart:cart'  # from cart app
        ]

    def location(self, item):
        return reverse(item)
