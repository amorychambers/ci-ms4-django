from django.contrib import admin
from .models import Product, Review

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'image',
        'rating',
        'description',
        'stock',
        'tags',
        'sale',
    )

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'product_id',
        'title',
        'date',
        'review_rating',
        'content',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)