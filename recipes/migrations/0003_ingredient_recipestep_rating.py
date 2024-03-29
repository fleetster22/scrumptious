# Generated by Django 4.2.1 on 2023-05-29 15:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_cook_time_recipe_prep_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(default=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='recipes.recipe')),
            ],
        ),
    ]
