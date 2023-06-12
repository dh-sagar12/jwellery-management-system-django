from django.db import models

from authentication.models import User
from product.models import ProductModel

# Create your models here.


class BannerImagesModel(models.Model):

    def banner_directory_path(instance, filename):
        return '{2}/{1}'.format(instance.id, filename, 'banners')

    id = models.AutoField(primary_key=True, db_column='id')
    banner_title = models.CharField(
        max_length=100, null=False, blank=False, db_column='banner_title')
    banner_image = models.ImageField(
        upload_to=banner_directory_path,  blank=True, db_column='banner_image')
    banner_redirect_url = models.CharField(
        max_length=100, blank=True, null=True, db_column='banner_redirect_url')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.banner_title

    class Meta:
        db_table = 'banner_images'


class FeatureProductModelManager(models.Manager):
    def set_single_main(self, instance):
        # Set active=False for all rows
        self.all().update(is_main=False)

        # Set active=True for the provided instance
        instance.is_main = True
        instance.save()


class FeatureProductModel(models.Model):
    def feature_directory_path(instance, filename):
        return '{2}/{1}'.format(instance.id, filename, 'features')

    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False, db_column='title')
    description = models.CharField(
        max_length=200, null=False, db_column='description')
    redirect_url = models.CharField(
        max_length=200, null=False, db_column='redirect_url')
    feature_image = models.ImageField(
        upload_to=feature_directory_path, blank=False, null=False, db_column='feature_image')
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)

    objects = FeatureProductModelManager()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'feature_products'


class MyCart(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, db_column='user_id')
    product_id = models.ForeignKey(
        ProductModel, on_delete=models.DO_NOTHING, db_column='product_id')
    cart_status = models.BooleanField(default=True, db_column='cart_status')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_id}'

    class Meta:
        db_table = 'cart'