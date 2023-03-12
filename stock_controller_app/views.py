from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import generic, View
from .models import Ingredient


class homePage(View):
    template_name = 'homepage.html'

    def get(self, request):
        return render(request, 'homepage.html')


class IngredientsList(generic.ListView):
    model = Ingredient
    template_name = 'index.html'
    paginate_by = 10


class addIngredient(View):
    def post(self, request, slug, *args, **kwargs):
        ingredient = get_object_or_404(Ingredient, slug=slug)
        ingredient.units += 1
        ingredient.save()

        return HttpResponseRedirect(reverse('home'))


class removeIngredient(View):
    def post(self, request, slug, *args, **kwargs):
        ingredient = get_object_or_404(Ingredient, slug=slug)
        ingredient.units -= 1
        ingredient.save()

        return HttpResponseRedirect(reverse('home'))


class showStockList(generic.ListView):
    model = Ingredient
    template_name = 'stock-list.html'
