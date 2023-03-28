from django.contrib import admin
from .models import Ingredient, Recipe, ingredientQuantity, IngredientsCalculation


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'units', 'price')
    search_fields = ['name']


@admin.register(Recipe)
class recipeAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(ingredientQuantity)
class ingredientsQuantity(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(IngredientsCalculation)
class ingredientsCalculation(admin.ModelAdmin):
    search_fields = ['recipe']
