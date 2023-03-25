from django.contrib import admin
from .models import Ingredient, Recipe, Quantity


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'units', 'price')
    search_fields = ['name']


@admin.register(Recipe)
class recipeAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Quantity)
class ingredientsQuantity(admin.ModelAdmin):
    search_fields = ['name']
