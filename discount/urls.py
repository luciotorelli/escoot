# discount/urls.py
from django.urls import path
from .views import validate_discount_code

app_name = 'discount'

urlpatterns = [
    path('validate/', validate_discount_code, name='validate_discount_code'),
]
