# Generated by Django 3.2.18 on 2023-03-21 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_controller_app', '0009_recipe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='solid_ingredients',
        ),
        migrations.AddField(
            model_name='recipe',
            name='solid_ingredients',
            field=models.ManyToManyField(to='stock_controller_app.Ingredient'),
        ),
    ]
