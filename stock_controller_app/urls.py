from . import views
from django.urls import path

urlpatterns = [
    path('', views.IngredientsList.as_view(), name='home')
]
