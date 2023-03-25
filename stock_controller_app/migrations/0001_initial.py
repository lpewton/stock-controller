# Generated by Django 3.2.18 on 2023-03-24 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('price', models.FloatField(default=0)),
                ('unit_weight', models.IntegerField(default=0)),
                ('units', models.IntegerField(default=1)),
                ('type', models.IntegerField(choices=[(0, 'Solid'), (1, 'Liquid')], default=0)),
                ('supplier', models.CharField(default='VILA', max_length=20)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ingredientsQuantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=500)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock_controller_app.ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('notes', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('ingredient', models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='stock_controller_app.ingredientsquantity')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
