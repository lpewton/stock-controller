from django.shortcuts import render
from django.views import generic
from .models import Ingredient


class IngredientsList(generic.ListView):
    model = Ingredient
    template_name = 'index.html'
    paginate_by = 10
