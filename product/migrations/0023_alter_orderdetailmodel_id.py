# Generated by Django 4.2.1 on 2023-06-09 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_rename_city_orderdetailmodel_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetailmodel',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
