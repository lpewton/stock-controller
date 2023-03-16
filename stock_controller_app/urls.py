from . import views
from django.urls import path

urlpatterns = [
    path('', views.homePage.as_view(), name='home'),
    path('ingredients-list', views.IngredientsList.as_view(), name='ingredients_list'),
    path('new-ingredient', views.newIngredient.as_view(), name='new_ingredient'),
    path('edit-ingredient/<slug:slug>', views.editIngredient.as_view(), name='edit_ingredient'),
    path('delete-ingredient/<slug:slug>', views.deleteIngredient.as_view(), name='delete_ingredient'),
    path('add-ingredient/<slug:slug>', views.addIngredient.as_view(), name='add_ingredient'),
    path('remove-ingredient/<slug:slug>', views.removeIngredient.as_view(), name='remove_ingredient'),
    path('stock-list', views.showStockList.as_view(), name='stock_list'),
]
