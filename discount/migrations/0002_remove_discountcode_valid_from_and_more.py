# Generated by Django 4.2.11 on 2024-05-29 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discountcode',
            name='valid_from',
        ),
        migrations.RemoveField(
            model_name='discountcode',
            name='valid_to',
        ),
    ]
