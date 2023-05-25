from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
# from django.http import HttpResponse
from recipes.models import Recipe
from recipes.forms import RecipeForm


# sends request to return a specific recipe based on id
def show_recipe(request, id):

    recipe = get_object_or_404(Recipe, id=id)

    context = {
        "recipe_object": recipe,
    }

    return render(request, "recipes/detail.html", context)


# sends request to return all recipes
def recipe_list(request):
    # recipes = Recipe.objects.all()
    recipes = get_list_or_404(Recipe)

    context = {
        "recipe_list": recipes,
     }
    return render(request, "recipes/list.html", context)


# validates data entered in form and pushes data to db
def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            # tells browser which page to go to after data is saved
            return redirect("recipe_list")

    else:
        form = RecipeForm()

    context = {
        "form": form,
    }
    return render(request, 'recipes/create.html', context)


def edit_recipe(request, id):

    recipe = get_object_or_404(Recipe, id=id)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            # tells browser which page to go to after data is saved
            return redirect("recipes/detail.html")

    else:
        form = RecipeForm(instance=recipe)

    context = {
        "recipe_object": recipe,
        "form": form,
    }
    return render(request, 'recipes/edit.html', context)
