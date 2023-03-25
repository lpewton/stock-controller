from django.contrib import admin
from .models import Ingredient, Recipe, solidsQuantity, liquidsQuantity


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'units', 'price')
    search_fields = ['name']


@admin.register(Recipe)
class recipeAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(solidsQuantity)
class ingredientsQuantity(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(liquidsQuantity)
class ingredientsQuantity(admin.ModelAdmin):
    search_fields = ['name']
