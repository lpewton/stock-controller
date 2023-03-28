from django import forms
from .models import Ingredient, Recipe, ingredientQuantity, IngredientsCalculation


class IngredientForm(forms.ModelForm):

    class Meta:
        model = Ingredient
        fields = ['name', 'price', 'unit_weight', 'units', 'supplier', 'type']


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ['name', 'ingredient', 'notes']


class IngredientQuantityForm(forms.ModelForm):

    class Meta:
        model = ingredientQuantity
        fields = ['name', 'quantity']


class IngredientsCalculationForm(forms.ModelForm):

    class Meta:
        model = IngredientsCalculation
        fields = ['recipe', 'quantity']
