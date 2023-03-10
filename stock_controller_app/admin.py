from django.contrib import admin
from .models import Ingredient


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'units', 'price')
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
