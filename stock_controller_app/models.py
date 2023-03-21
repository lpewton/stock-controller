from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Ingredient(models.Model):
    PRODUCT_TYPES = ((0, 'Solid'), (1, 'Liquid'))
    name = models.CharField(max_length=50, unique=True)
    price = models.FloatField(default=0)
    unit_weight = models.FloatField(default=0)
    image = CloudinaryField('image', default='placeholder')
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


class Recipe(models.Model):
    name = models.CharField(max_length=200, unique=True)
    solids = models.ManyToManyField(Ingredient, limit_choices_to={'type': 0}, related_name='solid_recipes')
    liquids = models.ManyToManyField(Ingredient, limit_choices_to={'type': 1}, related_name='liquid_recipes')
    intermediate_procedures = models.CharField(max_length=200, default='')
    add_ons = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name
