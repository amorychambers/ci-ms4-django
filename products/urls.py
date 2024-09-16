from django.urls import path
from products import views

urlpatterns = [
    path('', views.products, name='products'),
    path('product_details/<product_id>', views.product_details, name='product_details'),
]
