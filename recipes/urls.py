from django.urls import path
from recipes.views import show_recipe, recipe_list

urlpatterns = [
    # tells browser to navigate to recipes and then each recipe
    path('recipes/<int:id>', show_recipe),
    path('recipes/', recipe_list)
]
