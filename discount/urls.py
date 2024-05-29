from django.urls import path
from . import views

app_name = 'discount'

urlpatterns = [
    path('validate/', views.validate_discount_code, name='validate_discount_code'),
    path('', views.discount_list, name='discount_list'),
]
