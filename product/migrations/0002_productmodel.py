# Generated by Django 4.2.1 on 2023-06-05 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(db_column='product_name', max_length=200)),
                ('product_description', models.TextField(db_column='product_description', verbose_name='description')),
                ('purity', models.CharField(db_column='purity', max_length=20)),
                ('weight', models.IntegerField(db_column='weight', verbose_name='weight in Gram')),
                ('manufactured_date', models.DateField(auto_now_add=True, db_column='manufactured_date')),
                ('category', models.ManyToManyField(db_column='category', to='product.productcategorymodel')),
            ],
            options={
                'db_table': 'Product',
            },
        ),
    ]
