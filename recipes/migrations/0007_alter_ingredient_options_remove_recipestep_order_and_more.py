# Generated by Django 4.2.1 on 2023-05-30 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0006_recipestep'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ['food_item']},
        ),
        migrations.RemoveField(
            model_name='recipestep',
            name='order',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='amount',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='food_item',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='recipes.recipe'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cook_time',
            field=models.PositiveSmallIntegerField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prep_time',
            field=models.PositiveSmallIntegerField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipestep',
            name='instruction',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipestep',
            name='step_number',
            field=models.PositiveSmallIntegerField(default=True),
            preserve_default=False,
        ),
    ]
