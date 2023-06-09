# Generated by Django 4.2.1 on 2023-06-03 09:16

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannerimagesmodel',
            name='banner_image',
            field=models.ImageField(blank=True, db_column='banner_image', upload_to=home.models.BannerImagesModel.banner_directory_path),
        ),
        migrations.AlterField(
            model_name='bannerimagesmodel',
            name='banner_title',
            field=models.CharField(db_column='banner_title', max_length=100),
        ),
    ]
