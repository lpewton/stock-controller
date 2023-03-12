from . import views
from django.urls import path

urlpatterns = [
    path('', views.homePage.as_view(), name='home'),
    path('ingredients-list', views.IngredientsList.as_view(), name='ingredients_list'),
    path('add-ingredient/<slug:slug>', views.addIngredient.as_view(), name='add_ingredient'),
    path('remove-ingredient/<slug:slug>', views.removeIngredient.as_view(), name='remove_ingredient'),
    path('stock-list', views.showStockList.as_view(), name='stock_list'),
]
