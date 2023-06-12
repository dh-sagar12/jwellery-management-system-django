from django.contrib import admin
from .models import BannerImagesModel, FeatureProductModel, MyCart

# Register your models here.

@admin.register(BannerImagesModel)
class BannerImagesAdmin(admin.ModelAdmin):
    list_display = (
'id',
'banner_title',
'banner_redirect_url',
'is_active'
    )


@admin.register(FeatureProductModel)
class FeatureProductAdmin(admin.ModelAdmin):
    list_display = (
'id',
'title',
'description',
'redirect_url',
'is_active', 
'is_main'
    )



admin.site.register(MyCart)