# Generated by Django 3.2.7 on 2021-10-19 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_recipeingredient_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeingredient',
            name='quantity_as_float',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
