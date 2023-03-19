from django import forms
from .models import Ingredient


class IngredientForm(forms.ModelForm):

    class Meta:
        model = Ingredient
        fields = ['name', 'price', 'unit_weight', 'units', 'type', 'supplier']
