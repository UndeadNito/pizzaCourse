# Generated by Django 4.0.1 on 2022-01-09 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_rename_pizza_model_pizzamodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzamodel',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Pizza price'),
        ),
    ]
