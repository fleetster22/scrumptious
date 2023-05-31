from django.contrib import admin
from recipes.models import Recipe, RecipeStep, Ingredient

# Register your models here.
@admin.register(Recipe)

# below is what you want to display in the admin page
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "id",
    )

@admin.register(RecipeStep)
class RecipeStepAdmin(admin.ModelAdmin):
    list_display = (
        "step_number",
        "instruction",
        "id",

    )

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        "food_item",
        "amount",
        "id",
    )
