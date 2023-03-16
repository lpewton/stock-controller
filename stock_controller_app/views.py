from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from django.views import generic, View
from .models import Ingredient
from .forms import IngredientForm


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

        return HttpResponseRedirect(reverse('ingredients_list'))


class removeIngredient(View):
    def post(self, request, slug, *args, **kwargs):
        ingredient = get_object_or_404(Ingredient, slug=slug)
        ingredient.units -= 1
        ingredient.save()

        return HttpResponseRedirect(reverse('ingredients_list'))


class newIngredient(View):

    def post(self, request):
        form = IngredientForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('ingredients_list')

    def get(self, request):
        form = IngredientForm()
        context = {
            'form': form
        }

        return render(request, 'new-ingredient.html', context)


class editIngredient(View):

    def post(self, request, slug):
        ingredient = get_object_or_404(Ingredient, slug=slug)
        form = IngredientForm(request.POST, instance=ingredient)

        if form.is_valid():
            form.save()
            return redirect('ingredients_list')

    def get(self, request, slug):
        ingredient = get_object_or_404(Ingredient, slug=slug)
        form = IngredientForm(instance=ingredient)

        context = {
            'form': form,
            'ingredient': ingredient
        }

        return render(request, 'edit-ingredient.html', context)


class deleteIngredient(View):

    def post(self, request, slug, *args, **kwargs):
        ingredient = get_object_or_404(Ingredient, slug=slug)
        ingredient.delete()

        return HttpResponseRedirect(reverse('ingredients_list'))


class showStockList(generic.ListView):
    model = Ingredient
    template_name = 'stock-list.html'
