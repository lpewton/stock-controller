from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


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
    WORKER_TYPES = [
        ('scooper', 'Scooper'),
        ('cook', 'Cook'),
        ('stock-controller', 'Stock Controller')
    ]
    worker_type = forms.ChoiceField(choices=WORKER_TYPES)

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'worker_type')
