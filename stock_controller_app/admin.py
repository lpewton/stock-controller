from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'units', 'unit_price')
    search_fields = ['name']


@admin.register(Recipe)
class recipeAdmin(admin.ModelAdmin):
    search_fields = ['recipe_name']


@admin.register(ingredientQuantity)
class ingredientsQuantityAdmin(admin.ModelAdmin):
    list_display = ('ingredient_name', 'quantity')


# Authorized Users
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'worker_type', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('worker_type',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
