from django.db import models
from cloudinary.models import CloudinaryField

class Product(models.Model):
    """Model representing a product."""
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    image = CloudinaryField('image')  # Uses CloudinaryField
    status = models.CharField(max_length=255)
    product_category = models.CharField(max_length=255)

    def __str__(self):
        """
        Get a human-readable representation of the product.

        Returns:
            str: The product name of the product.
        """
        return self.product_name