from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

class Review(models.Model):
    """
    A model to store user reviews of products on the site
    """

    review_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=False, blank=False, default='')

    def __str__(self):
        return f"{self.review_product.name} review by {self.user.username}"
