from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Ingredient(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.FloatField()
    unit_weight = models.FloatField(default=0)
    image = CloudinaryField('image', default='placeholder')
    units = models.IntegerField()

    def __str__(self):
        return self.name
