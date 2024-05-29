# Generated by Django 4.2.11 on 2024-05-28 20:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='products',
            field=models.ManyToManyField(related_name='wishlists', to='products.product'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='WishlistItem',
        ),
    ]