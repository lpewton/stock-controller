from django import forms
from .models import Ingredient


class IngredientForm(forms.ModelForm):

    class Meta:
        model = Ingredient
        fields = ['name','slug', 'price', 'unit_weight', 'units', 'type', 'supplier']
