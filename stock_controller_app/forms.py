from django import forms
from .models import Ingredient, Recipe, ingredientQuantity, IngredientsCalculation
from django.contrib.auth.forms import UserCreationForm


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


class CustomUserCreationForm(UserCreationForm):
    worker_type = forms.Select()

    class Meta:
        fields = ['username', 'worker-type', 'password1', 'password2']
