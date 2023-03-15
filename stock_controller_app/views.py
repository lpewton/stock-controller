from django.shortcuts import render, get_object_or_404, reverse, redirect
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

        return HttpResponseRedirect(reverse('ingredients_list'))


class removeIngredient(View):
    def post(self, request, slug, *args, **kwargs):
        ingredient = get_object_or_404(Ingredient, slug=slug)
        ingredient.units -= 1
        ingredient.save()

        return HttpResponseRedirect(reverse('ingredients_list'))


class newIngredient(View):
    template_name = 'new-ingredient.html'

    def get(self, request):
        return render(request, 'new-ingredient.html')

    def post(self, request):
        if request.method == 'POST':

            name = request.POST.get('ingredient_name')
            slug = request.POST.get('ingredient_name')
            price = request.POST.get('ingredient_price')
            unit_weight = request.POST.get('ingredient_unit_weight')
            units = request.POST.get('ingredient_units')
            type = request.POST.get('ingredient_type')
            supplier = request.POST.get('ingredient_supplier')

            Ingredient.objects.create(
                name=name, price=price, slug=slug, unit_weight=unit_weight, units=units, type=type, supplier=supplier)
            return redirect('ingredients_list')


class showStockList(generic.ListView):
    model = Ingredient
    template_name = 'stock-list.html'
