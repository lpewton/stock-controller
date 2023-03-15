from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Ingredient(models.Model):
    PRODUCT_TYPES = ((0, 'solid'), (1, 'liquid'))
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    price = models.FloatField(default=0)
    unit_weight = models.FloatField(default=0)
    image = CloudinaryField('image', default='placeholder')
    units = models.IntegerField(default=1)
    type = models.IntegerField(choices=PRODUCT_TYPES, default=0)
    supplier = models.CharField(max_length=20, default='VILA')

    prepopulated_fields = {'slug': ('name',)}

    def __str__(self):
        return self.name

    def weight_value(self):
        return self.unit_weight * self.units

    def price_value(self):
        return self.price * self.units

    class Meta:
        ordering = ["name"]
