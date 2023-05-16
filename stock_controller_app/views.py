from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import TemplateView, ListView, DetailView, View
from django.db.models import Q
from .models import *
from .forms import *
from django.contrib import messages


# Login
class homePage(TemplateView):
    """Render the landing page"""
    template_name = 'index.html'


# Search Bar
class IngredientSearchResults(generic.ListView):
    """
    View for rendering the ingredient search results page
    """
    template_name = 'search-ingredients.html'
    paginate_by = 4

    def querystring(self):
        """
        querystring method
        Required for retaining the same queryset across multiple -
        - pagination pages
        """
        querystring = self.request.GET.copy()
        querystring.pop(self.page_kwarg, None)
        encoded_querystring = querystring.urlencode()
        return encoded_querystring

    def get_queryset(self):
        """
        get_queryset method
        Constructs a queryset using Q methods
        Returns an object_list for use within the template
        """
        query = self.request.GET.get('search')
        ingredients_list = Ingredient.objects.filter(
            Q(name__icontains=query) |
            Q(supplier__icontains=query)
            )
        return ingredients_list


class RecipeSearchResults(generic.ListView):
    """
    View for rendering the recipe search results page
    """
    template_name = 'search-recipes.html'
    paginate_by = 4

    def querystring(self):
        """
        querystring method
        Required for retaining the same queryset across multiple -
        - pagination pages
        """
        querystring = self.request.GET.copy()
        querystring.pop(self.page_kwarg, None)
        encoded_querystring = querystring.urlencode()
        return encoded_querystring

    def get_queryset(self):
        """
        get_queryset method
        Constructs a queryset using Q methods
        Returns an object_list for use within the template
        """
        query = self.request.GET.get('search')
        recipes_list = Recipe.objects.filter(
            Q(recipe_name__icontains=query)
            )
        return recipes_list


# Ingredients
class IngredientsList(ListView):
    """Render ingredients list page"""
    model = Ingredient
    template_name = 'ingredients-list.html'
    paginate_by = 8


class addIngredient(View):
    """Adds to the value of the ingredient's units"""
    def post(self, request, pk=None):
        ingredient = get_object_or_404(Ingredient, pk=pk)
        ingredient.units += 1
        ingredient.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class removeIngredient(View):
    """Substracts from the value of the ingredient's units"""
    def post(self, request, pk):
        ingredient = get_object_or_404(Ingredient, pk=pk)
        ingredient.units -= 1
        ingredient.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


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
            ingredient = form.save(commit=False)
            # Capitalise names so they're not repeated
            ingredient.name = form.cleaned_data['name'].title()
            ingredient.save()
            messages.success(request, "Ingredient added successfully")

            return redirect('ingredients_list')

        else:
            messages.error(
                request, "Please make sure all inputs are correct\
                or the ingredient doesn't already exist")

            return redirect('new_ingredient')


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
            ingredient = form.save(commit=False)
            # Capitalise names so they're not repeated
            ingredient.name = form.cleaned_data['name'].title()
            ingredient.save()
            messages.success(request, "Ingredient edited successfully")

            return redirect('ingredients_list')

        else:
            messages.error(
                request, "Please make sure all inputs are correct\
                or the ingredient doesn't already exist")

            return redirect('new_ingredient')


class deleteIngredient(View):
    """Deletes ingredient"""

    def post(self, request, pk):
        try:
            ingredient = get_object_or_404(Ingredient, pk=pk)
            ingredient.delete()
            messages.success(request, "Ingredient deleted successfully")
        except Exception as e:
            messages.error(request, "Couldn't delete ingredient as\
            it's part of a recipe, please delete recipe first")

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
    paginate_by = 12


class addRecipe(View):
    """Adds to the value of the recipe's tubs"""
    def post(self, request, pk=None):
        recipe = get_object_or_404(Recipe, pk=pk)
        recipe.tubs += 1
        recipe.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class removeRecipe(View):
    """Substracts from the value of the recipe's units"""
    def post(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        recipe.tubs -= 1
        recipe.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class deleteRecipe(View):
    """Deletes recipe"""

    def post(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)

        # Delete ingredient quantities when recipes are deleted
        for ingredient in recipe.ingredient.all():
            if Recipe.objects.filter(
                 ingredient=ingredient).exclude(pk=pk).exists():
                continue
            ingredient.delete()

        recipe.delete()
        messages.success(request, "Recipe deleted successfully")
        return HttpResponseRedirect(reverse('recipes'))


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
            recipe = recipeForm.save(commit=False)
            # Capitalise names so they're not repeated
            recipe.recipe_name = recipeForm.cleaned_data['recipe_name'].title()
            recipeForm.save()
            messages.success(request, "Recipe added successfully")

            return redirect('recipes')

        else:
            messages.error(request, "Could not add recipe")

            return redirect('recipes')

        if ingredientQuantityForm.is_valid():
            ingredientQuantityForm.save()

            return redirect('new_recipe')

        else:
            messages.error(
                request, "Ingredient quantity already exists\
                    or quantity is smaller than 1g")

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
            recipe = ingredientsCalculationForm.cleaned_data['recipe']
            quantity = ingredientsCalculationForm.cleaned_data['quantity']

            # Make sure recipes don't repeat themselves
            if IngredientsCalculation.objects.filter(recipe=recipe).exists():
                existing_calculation = IngredientsCalculation.objects.get(
                    recipe=recipe)
                existing_calculation.quantity += quantity
                existing_calculation.save()
            else:
                ingredients_calculation = ingredientsCalculationForm.save()

        else:
            messages.error(request, "Could not add ice cream, please make sure\
                quantities are larger than 0")
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


# Register a new user
class signup(View):
    def get(self, request):
        context = {
            "user_form": UserCreationForm()
        }
        return render(request, 'signup.html', context)

    def post(self, request):
        signup_form = CustomUserCreationForm(request.POST)

        username = request.POST['username']
        worker_type = request.POST['worker_type']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if signup_form.is_valid():
            signup_form.save()
            messages.success(request, "New user added successfully")
            return redirect('ingredients_list')
        else:
            messages.error(
                request, "Something went wrong, please make sure password is\
                    long enough and contains letters and numbers or user\
                        doesn't exist")

            return redirect('signup')
