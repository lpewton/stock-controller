# Generated by Django 3.2.18 on 2023-04-27 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock_controller_app', '0005_delete_ingredientpricesum'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntermediateRecipeIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock_controller_app.ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock_controller_app.recipe')),
            ],
        ),
    ]