# Generated by Django 4.2.1 on 2023-06-05 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_productmodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='price',
            field=models.DecimalField(db_column='price', decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='weight',
            field=models.DecimalField(db_column='weight', decimal_places=3, max_digits=10, verbose_name='weight in Gram'),
        ),
    ]
