# Generated by Django 4.2.11 on 2024-05-21 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('in-stock', 'Stocked'), ('out-of-stock', 'Out of Stock'), ('deactivated', 'Deactivated')], max_length=20),
        ),
    ]
