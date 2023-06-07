# Generated by Django 4.2.1 on 2023-06-05 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_productmodel_is_active_productmodel_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='slug',
            field=models.SlugField(db_column='slug', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='is_active',
            field=models.BooleanField(db_column='is_active', default=True, verbose_name='Active'),
        ),
    ]
