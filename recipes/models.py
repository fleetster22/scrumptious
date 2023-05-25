from django.db import models

# Create models here
class Recipe(models.Model):

    title = models.CharField(max_length=200)
    picture = models.URLField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    prep_time = models.PositiveSmallIntegerField(null=True)
    cook_time = models.PositiveSmallIntegerField(null=True)
