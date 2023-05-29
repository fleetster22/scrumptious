from django.forms import ModelForm
from recipes.models import Recipe, Rating

class RecipeForm(ModelForm):

    class Meta:
        model = Recipe
        fields = [
            "title",
            "picture",
            "description",
            "prep_time",
            "cook_time",
        ]


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ["value"]
