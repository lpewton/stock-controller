from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import TemplateView, ListView, DetailView, View
from .models import Ingredient, Recipe
from .forms import IngredientForm


class homePage(TemplateView):
    """Render the landing page"""
    template_name = 'homepage.html'


class IngredientsList(ListView):
    """Render index page"""
    model = Ingredient
    template_name = 'index.html'
    paginate_by = 10


class addIngredient(View):
    """Adds to the value of the ingredient's units"""
    def post(self, request, pk=None):
        ingredient = get_object_or_404(Ingredient, pk=pk)
        ingredient.units += 1
        ingredient.save()

        return HttpResponseRedirect(reverse('ingredients_list'))


class removeIngredient(View):
    """Substracts from the value of the ingredient's units"""
    def post(self, request, pk):
        ingredient = get_object_or_404(Ingredient, pk=pk)
        ingredient.units -= 1
        ingredient.save()

        return HttpResponseRedirect(reverse('ingredients_list'))


class newIngredient(TemplateView):
    """Render new ingredient page"""

    def get(self, request):
        form = IngredientForm()
        context = {
            'form': form
        }

        return render(request, 'new-ingredient.html', context)

    def post(self, request):
        form = IngredientForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('ingredients_list')


class editIngredient(DetailView):
    """Render edit ingredient page"""

    def get(self, request, pk):
        ingredient = get_object_or_404(Ingredient, pk=pk)
        form = IngredientForm(instance=ingredient)

        context = {
            'form': form,
            'ingredient': ingredient
        }

        return render(request, 'edit-ingredient.html', context)

    def post(self, request, pk):
        ingredient = get_object_or_404(Ingredient, pk=pk)
        form = IngredientForm(request.POST, instance=ingredient)

        if form.is_valid():
            form.save()
            return redirect('ingredients_list')


class deleteIngredient(View):
    """Deletes ingredient"""

    def post(self, request, pk):
        ingredient = get_object_or_404(Ingredient, pk=pk)
        ingredient.delete()

        return HttpResponseRedirect(reverse('ingredients_list'))


class showStockList(ListView):
    """Renders stock list page"""
    model = Ingredient
    template_name = 'stock-list.html'


class recipes(ListView):
    """Render recipes list page"""
    model = Recipe
    template_name = 'recipes.html'
    paginate_by = 12


class recipeDetail(DetailView):
    model = Recipe
    template_name = 'recipe-detail.html'
