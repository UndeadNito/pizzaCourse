# Generated by Django 4.0.1 on 2022-01-16 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_pizzamodel_price'),
        ('cart', '0004_orderlist_done'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='object_id',
        ),
        migrations.AddField(
            model_name='item',
            name='object',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.pizzamodel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderlist',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.customer', verbose_name='Customer'),
        ),
        migrations.AlterField(
            model_name='orderlist',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.pizzamodel', verbose_name='Product'),
        ),
    ]
