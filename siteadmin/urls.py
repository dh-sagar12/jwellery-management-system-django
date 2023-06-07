from django.urls import path
from product.views import AddCategoryPage, AddInventoryPage, ManageCategoryPage, EditCategory, ManageInventoryPage, ManageProductPage, AddProductPage, EditProduct
from . import views



urlpatterns = [
    path('', views.AdminHomePage, name='AdminHomePage'),
    path('setting/', views.SettingPage, name='SettingPage'),
    path('category/', ManageCategoryPage, name='ManageCategoryPage'),
    path('category/new', AddCategoryPage, name='AddCategoryPage'),
    path('category/<int:id>', EditCategory, name='EditCategory'),
    path('product/', ManageProductPage, name='ManageProductPage'),
    path('product/new', AddProductPage, name='AddProductPage'),
    path('product/<int:id>', EditProduct, name='EditProduct'),
    path('inventory/', ManageInventoryPage, name='ManageInventoryPage'),
    path('inventory/new', AddInventoryPage, name='AddInventoryPage')

]