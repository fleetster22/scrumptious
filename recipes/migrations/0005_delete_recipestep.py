# Generated by Django 4.2.1 on 2023-05-30 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_recipestep_instruction_recipestep_order_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RecipeStep',
        ),
    ]
