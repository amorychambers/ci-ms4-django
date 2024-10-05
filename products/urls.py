from django.urls import path
from products import views
from reviews import views as review_views

urlpatterns = [
    path('', views.products, name='products'),
    path('product_details/<product_id>', views.product_details, name='product_details'),
    path('add_product', views.add_product, name='add_product'),
    path('update_product/<product_id>', views.update_product, name='update_product'),
    path('delete_product/<product_id>', views.delete_product, name='delete_product'),
    path('delete_review/<review_id>', review_views.delete_review, name='delete_review'),
]
