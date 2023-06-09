from django.contrib import admin

from product.models import OrderDetailModel, ProductCategoryModel, ProductModel

# Register your models here.
@admin.register(ProductCategoryModel)
class FeatureProductAdmin(admin.ModelAdmin):
    list_display = (
    'id',
    'category_name',
    'category_url_name' 
    )


admin.site.register(ProductModel)
admin.site.register(OrderDetailModel)