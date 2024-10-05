from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.


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
    sale = models.DecimalField(max_digits=4, decimal_places=2,
                               null=True, blank=True)

    def get_sale_price(self):
        if self.sale:
            return round(self.price * self.sale, 2)
        else:
            return self.price

    def __str__(self):
        return self.name
