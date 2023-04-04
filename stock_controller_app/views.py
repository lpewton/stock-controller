from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import TemplateView, ListView, DetailView, View
from .models import Ingredient, Recipe, ingredientQuantity, IngredientsCalculation, final_ic_list
from .forms import IngredientForm, RecipeForm, IngredientQuantityForm, IngredientsCalculationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class homePage(TemplateView):
    """Render the landing page"""
    template_name = 'homepage.html'


# Ingredients
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


# Recipes
class recipes(ListView):
    """Render recipes list page"""
    model = Recipe
    template_name = 'recipes.html'
    paginate_by = 15


class recipeDetail(DetailView):
    """Renders the details of each recipe"""
    model = Recipe
    template_name = 'recipe-detail.html'
    context_object_name = 'recipe'


class newRecipe(TemplateView):
    """Renders new recipe page"""
    def get(self, request):
        recipeForm = RecipeForm
        ingredientQuantityForm = IngredientQuantityForm
        context = {
            'RecipeForm': RecipeForm,
            'IngredientQuantityForm': IngredientQuantityForm
        }

        return render(request, 'new-recipe.html', context)

    def post(self, request):
        recipeForm = RecipeForm(request.POST)
        ingredientQuantityForm = IngredientQuantityForm(request.POST)

        if recipeForm.is_valid():
            recipeForm.save()
            return redirect('recipes')

        elif ingredientQuantityForm.is_valid():
            ingredientQuantityForm.save()
            return redirect('new_recipe')


# Recipes Calculations
class ingredientsCalculation(View):
    """Renders Ingredient Calculation page"""
    def get(self, request):
        model = IngredientsCalculation
        context = {
            'IngredientsCalculationForm': IngredientsCalculationForm,
            'ingredients': IngredientsCalculation.objects.all
        }
        return render(request, 'ingredients-calculation.html', context)

    def post(self, request):
        ingredientsCalculationForm = IngredientsCalculationForm(request.POST)

        if ingredientsCalculationForm.is_valid():
            ingredientsCalculationForm.save()
            return redirect('ingredients_calculation')


class resetIngredients(View):
    """Resets Ingredients Calculation list"""
    def post(self, request):
        IngredientsCalculation.objects.all().delete()

        return HttpResponseRedirect(reverse('ingredients_calculation'))


class ingredientsResult(View):
    """Calculates how many ingredients are needed for an X number of recipes"""
    def get(self, request):
        final_ic_list.clear()
        model = IngredientsCalculation
        context = {
            'final_ic_list': final_ic_list,
            'recipes': IngredientsCalculation.objects.all
        }

        return render(request, 'ingredients-result.html', context)


class signup(View):
    def get(self, request):
        context = {
            'signup_form': UserCreationForm()
        }

        return render(request, 'signup.html', context)
