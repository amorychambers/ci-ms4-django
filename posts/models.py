from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

class Post(models.Model):
    """
    A model for community submitted posts
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=256, null=False, blank=False)
    date = models.DateField(auto_now_add=True)
    content = models.TextField(null=False, blank=False, default='')
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.user}"
