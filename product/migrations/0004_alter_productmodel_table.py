# Generated by Django 4.2.1 on 2023-06-05 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_productmodel_category_productmodel_categories'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='productmodel',
            table='product',
        ),
    ]
