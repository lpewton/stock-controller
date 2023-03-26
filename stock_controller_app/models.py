from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Ingredient(models.Model):
    PRODUCT_TYPES = ((0, 'Solid'), (1, 'Liquid'))
    name = models.CharField(max_length=50, unique=True)
    price = models.FloatField(default=0)
    unit_weight = models.IntegerField(default=0)
    units = models.IntegerField(default=1)
    type = models.IntegerField(choices=PRODUCT_TYPES, default=0)
    supplier = models.CharField(max_length=20, default='VILA')

    def __str__(self):
        return self.name

    def weight_value(self):
        return self.unit_weight * self.units

    def price_value(self):
        return self.price * self.units

    class Meta:
        ordering = ["name"]


class ingredientQuantity(models.Model):
    name = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=500)

    def __str__(self):
        return f"{self.name} ({self.quantity}g)"

    class Meta:
        ordering = ["name"]


class Recipe(models.Model):
    name = models.CharField(max_length=200, unique=True)
    ingredient = models.ManyToManyField(ingredientQuantity)
    notes = models.CharField(max_length=200, default='', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
