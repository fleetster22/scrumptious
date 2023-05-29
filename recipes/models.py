from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

#Get the name of the class for the User
USER_MODEL = settings.AUTH_USER_MODEL

# Create models here
class Recipe(models.Model):

#     author = models.ForeignKey(
#     USER_MODEL,
#     related_name="recipes",
#     on_delete=models.CASCADE,
#     null=True,
# )

    title = models.CharField(max_length=200)
    picture = models.URLField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    prep_time = models.PositiveSmallIntegerField(null=True)
    cook_time = models.PositiveSmallIntegerField(null=True)


class Ingredient(models.Model):
    pass


class RecipeStep(models.Model):
    pass

# Create a many-to-one association. many recipes-one author
# The one side contains the primary key, the many side has the foreign key



class Rating(models.Model):
    value = models.PositiveSmallIntegerField(
        default=5, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    recipe = models.ForeignKey(
        "Recipe", related_name="ratings", on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.value)
