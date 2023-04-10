from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser

names_ic_list = []
final_ic_list = []


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


class IngredientsCalculation(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.recipe} ({self.quantity}L)"

    def recipe_ingredients(self):

        ingredients = self.recipe.ingredient.all()

        for ingredient in ingredients:
            ingredient_name = f'{ingredient.name}'
            matching_item = next((item for item in final_ic_list if ingredient_name in item), None)

            if matching_item is None:
                new_quantity = ingredient.quantity * self.quantity
                final_ic_list.append(f'{ingredient.name}, {new_quantity}')
            else:
                removed_index = final_ic_list.index(matching_item)

                split_list = final_ic_list[removed_index].split(',')
                new_quantity = int(split_list[1]) + (ingredient.quantity * self.quantity)

                final_ic_list.pop(removed_index)

                final_ic_list.append(f'{ingredient.name}, {new_quantity}')
                final_ic_list.sort()

        return self


class CustomUser(AbstractUser):
    WORKER_TYPES = (
        ('scooper', 'Scooper'),
        ('cook', 'Cook'),
        ('stock-controller', 'Stock Controller'),
    )

    worker_type = models.CharField(max_length=50, choices=WORKER_TYPES, default='scooper')
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        related_query_name='customuser',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        related_query_name='customuser',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )