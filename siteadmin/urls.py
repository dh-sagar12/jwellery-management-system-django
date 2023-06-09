from django.urls import path
from product.views import AddCategoryPage, AddInventoryPage, ManageCategoryPage, EditCategory, ManageInventoryPage, ManageProductPage, AddProductPage, EditProduct
from .views import AddBannerImagesPage, AddFeatureProductPage, EditBannerImages, EditFeatureProduct, ManageBannerImagesPage, ManageFeatureProductPage, SettingPage, AdminHomePage



urlpatterns = [
    path('', AdminHomePage, name='AdminHomePage'),
    path('setting/', SettingPage, name='SettingPage'),
    path('category/', ManageCategoryPage, name='ManageCategoryPage'),
    path('category/new', AddCategoryPage, name='AddCategoryPage'),
    path('category/<int:id>', EditCategory, name='EditCategory'),
    path('product/', ManageProductPage, name='ManageProductPage'),
    path('product/new', AddProductPage, name='AddProductPage'),
    path('product/<int:id>', EditProduct, name='EditProduct'),
    path('inventory/', ManageInventoryPage, name='ManageInventoryPage'),
    path('inventory/new', AddInventoryPage, name='AddInventoryPage'), 
    path('featureproduct/', ManageFeatureProductPage, name='ManageFeatureProductPage'), 
    path('featureproduct/new', AddFeatureProductPage, name='AddFeatureProductPage'), 
    path('featureproduct/<int:id>', EditFeatureProduct, name='EditFeatureProduct'),
    path('bannerimage/', ManageBannerImagesPage, name='ManageBannerImagesPage'), 
    path('bannerimage/new', AddBannerImagesPage, name='AddBannerImagesPage'), 
    path('bannerimage/<int:id>', EditBannerImages, name='EditBannerImages')

]