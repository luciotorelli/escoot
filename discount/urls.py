# discount/urls.py
from django.urls import path
from .views import apply_discount

app_name = 'discount'

urlpatterns = [
    path('apply/', apply_discount, name='apply_discount'),
]
