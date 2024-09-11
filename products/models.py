from django.db import models
from django.contrib.postgres.fields import ArrayField

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
    }

    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    rating = ArrayField(models.IntegerField(choices=RATING_CHOICES), default=list())
    description = models.TextField()
    stock = models.IntegerField(default=0)
    tags = ArrayField(models.CharField(max_length=64, choices=TAG_CHOICES), default=list())
    sale = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)


    def get_rating(self):
        if len(self.rating) > 0:
            average = sum(self.rating)/len(self.rating)
            return average
        else:
            return 'No Ratings'

    def __str__(self):
        return self.name
    
    