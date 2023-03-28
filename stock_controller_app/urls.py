from . import views
from django.urls import path

urlpatterns = [
    path('', views.homePage.as_view(), name='home'),
    path('ingredients-list', views.IngredientsList.as_view(),
         name='ingredients_list'),
    path('new-ingredient', views.newIngredient.as_view(),
         name='new_ingredient'),
    path('edit-ingredient/<int:pk>', views.editIngredient.as_view(),
         name='edit_ingredient'),
    path('delete-ingredient/<int:pk>', views.deleteIngredient.as_view(),
         name='delete_ingredient'),
    path('add-ingredient/<int:pk>', views.addIngredient.as_view(),
         name='add_ingredient'),
    path('remove-ingredient/<int:pk>', views.removeIngredient.as_view(),
         name='remove_ingredient'),
    path('stock-list', views.showStockList.as_view(), name='stock_list'),
    path('recipes', views.recipes.as_view(), name='recipes'),
    path('recipe/<int:pk>', views.recipeDetail.as_view(),
         name='recipe_detail'),
    path('new-recipe', views.newRecipe.as_view(), name='new_recipe'),
    path('ingredients-calculation', views.ingredientsCalculation.as_view(),
         name='ingredients_calculation')
]
