# Generated by Django 4.0.1 on 2022-01-16 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_remove_item_object_id_item_object_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='price',
        ),
    ]
