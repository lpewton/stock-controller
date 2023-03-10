from . import views
from django.urls import path

urlpatterns = [
    path('', views.IngredientsList.as_view(), name='home'),
    path('add-ingredient/<slug:slug>', views.addIngredient.as_view(), name='add_ingredient'),
    path('remove-ingredient/<slug:slug>', views.removeIngredient.as_view(), name='remove_ingredient'),
]
