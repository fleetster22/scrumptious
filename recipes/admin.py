from django.contrib import admin
from recipes.models import Recipe

# Register your models here.
@admin.register(Recipe)

# below is what you want to display in the admin page
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "id"
    )
