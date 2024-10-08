from django.urls import path
from profiles import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('delete_account', views.delete_account, name="delete_account")
]
