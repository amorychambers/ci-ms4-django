from django.contrib import admin
from .models import Review

# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'review_product',
        'title',
        'date',
        'content',
    )

admin.site.register(Review, ReviewAdmin)