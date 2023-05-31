from django.db import models
from django.conf import settings


# Create models here
class Recipe(models.Model):

    title = models.CharField(max_length=200)
    picture = models.URLField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    prep_time = models.PositiveSmallIntegerField()
    cook_time = models.PositiveSmallIntegerField()

# Create a many-to-one association
# author must be logged in to create recipe
    author = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    related_name="recipes",
    on_delete=models.CASCADE,
    null=True,
)
    def __str__(self):
        return self.title

# The one side contains the primary key, the many side has the foreign key
class RecipeStep(models.Model):
    step_number = models.PositiveSmallIntegerField()
    instruction = models.TextField()

    # makes sure steps stay in order
    # recipe is the variable name of the foreign key
    recipe = models.ForeignKey(
        # Recipe is the related table
        Recipe,
        # steps is the variable name for the RecipeStep table so you can
        # reference recipe.steps
        related_name="steps",
        on_delete=models.CASCADE,
        null=True,
    )
    class Meta:
        ordering = ["step_number"]


class Ingredient(models.Model):
    amount = models.CharField(max_length=100)
    food_item = models.CharField(max_length=100)

    recipe = models.ForeignKey(
        Recipe,
        related_name="ingredients",
        on_delete=models.CASCADE,
    )
    class Meta:
        ordering = ["food_item"]
