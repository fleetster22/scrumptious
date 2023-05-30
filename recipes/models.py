from django.db import models
from django.conf import settings
# from django.core.validators import MaxValueValidator, MinValueValidator

#Get the name of the class for the User
USER_MODEL = settings.AUTH_USER_MODEL

# Create models here
class Recipe(models.Model):



    title = models.CharField(max_length=200)
    picture = models.URLField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    prep_time = models.PositiveSmallIntegerField(null=True)
    cook_time = models.PositiveSmallIntegerField(null=True)

# Create a many-to-one association
# author must be logged in to create recipe
#     author = models.ForeignKey(
#     USER_MODEL,
#     related_name="recipes",
#     on_delete=models.CASCADE,
#     null=True,
# )


# The one side contains the primary key, the many side has the foreign key
# class RecipeStep(models.Model):
#     instruction = models.TextField(null=True)
#     # makes sure steps stay in order
#     order = models.PositiveSmallIntegerField(null=True)
#     # recipe is the variable name of the foreign key
#     recipe = models.ForeignKey(
#         # Recipe is the related table
#         Recipe,
#         # steps is the variable name for the RecipeStep table so you can
#         # reference recipe.steps
#         related_name="steps",
#         on_delete=models.CASCADE,
#         null=True,
#     )
#     class Meta:
#         pass

class Ingredient(models.Model):
    pass
