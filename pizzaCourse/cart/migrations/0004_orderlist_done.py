# Generated by Django 4.0.1 on 2022-01-14 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_rename_customer_id_orderlist_customer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlist',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
