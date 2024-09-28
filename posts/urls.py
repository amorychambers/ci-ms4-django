from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('create_post/', views.create_post, name='create_post'),
    path('delete_post/<post_id>', views.delete_post, name='delete_post'),
]
