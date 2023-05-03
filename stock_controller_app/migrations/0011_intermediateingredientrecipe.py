# Generated by Django 3.2.18 on 2023-05-02 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock_controller_app', '0010_alter_ingredientscalculation_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntermediateIngredientRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock_controller_app.ingredientquantity')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock_controller_app.recipe')),
            ],
        ),
    ]