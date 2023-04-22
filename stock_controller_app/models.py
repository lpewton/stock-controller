from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

names_ic_list = []
final_ic_list = []


class Ingredient(models.Model):
    PRODUCT_TYPES = ((0, 'Solid'), (1, 'Liquid'), (3, 'Non-Edibles'))
    name = models.CharField(max_length=50, unique=True)
    price = models.FloatField(validators=[MinValueValidator(0.01)])
    unit_weight = models.PositiveIntegerField(validators=[MinValueValidator(1)], default=1)
    units = models.PositiveIntegerField(default=1)
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
    ingredient_name = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)], default=500)

    def __str__(self):
        return f"{self.ingredient_name} ({self.quantity}g)"

    class Meta:
        ordering = ["ingredient_name"]
        unique_together = ["ingredient_name", "quantity"]


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200, unique=True)
    ingredient = models.ManyToManyField(ingredientQuantity)
    notes = models.CharField(max_length=200, default='', null=True, blank=True)

    def __str__(self):
        return self.recipe_name

    class Meta:
        ordering = ["recipe_name"]

    def recipe_quantity(self):

        ingredients = self.ingredient.all()
        recipe_quantity = 0

        for ingredient in ingredients:
            recipe_quantity += ingredient.quantity
        return recipe_quantity

    def recipe_cost(self):

        ingredients = self.ingredient.all()
        ingredient_list = []

        for ingredient in ingredients:
            ingredient_int = (ingredient.ingredient_name.price * ingredient.quantity) / 1000
            ingredient_list.append(ingredient_int)

        recipe_cost = round(sum(ingredient_list), 2)

        return recipe_cost

    def profit_medium(self):
        return round(((self.recipe_quantity() / 120) * 3.8) - self.recipe_cost(), 2)


class IngredientsCalculation(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.recipe} ({self.quantity}L)"

    def recipe_ingredients(self):

        ingredients = self.recipe.ingredient.all()

        for ingredient in ingredients:
            ingredient_name = f'{ingredient.ingredient_name}'
            matching_item = next((
                item for item in final_ic_list if ingredient_name in item),
                    None)

            if matching_item is None:
                new_quantity = ingredient.quantity * self.quantity
                final_ic_list.append(
                    f'{ingredient.ingredient_name},{new_quantity}')
            else:
                removed_index = final_ic_list.index(matching_item)

                split_list = final_ic_list[removed_index].split(',')
                new_quantity = int(split_list[1]) + (
                    ingredient.quantity * self.quantity)

                final_ic_list.pop(removed_index)

                final_ic_list.append(f'{ingredient.ingredient_name}, {new_quantity}')
                final_ic_list.sort()

        return self


class CustomUser(AbstractUser):
    WORKER_TYPES = (
        ('scooper', 'Scooper'),
        ('cook', 'Cook'),
        ('stock-controller', 'Stock Controller'),
    )

    worker_type = models.CharField(
        max_length=50, choices=WORKER_TYPES, default='scooper')
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        related_query_name='customuser',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        related_query_name='customuser',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )
