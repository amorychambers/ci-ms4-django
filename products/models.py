from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from multiselectfield import MultiSelectField

# Create your models here.

RATING_CHOICES = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five"
}

class Product(models.Model):
    TAG_CHOICES = {
        "coffee": "Coffee",
        "equipment": "Equipment",
        "single": "Single Origin",
        "blend": "Blend",
        "sale": "Sale",
        "bundle": "Bundle"
    }

    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    stock = models.IntegerField(default=0)
    tags = MultiSelectField(choices=TAG_CHOICES)
    sale = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
        
    def get_sale_price(self):
        if self.sale:
            return round(self.price * self.sale, 2)
        else:
            return self.price

    def __str__(self):
        return self.name
    
class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    date = models.DateField(auto_now_add=True)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} Review: Product ID {self.product_id}"