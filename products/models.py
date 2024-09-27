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
        "seasonal": "Seasonal",
        "sale": "Sale",
        "bundle": "Bundles"
    }

    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=False)
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