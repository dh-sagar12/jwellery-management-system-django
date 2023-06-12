from django.urls import path
from . import views



urlpatterns = [
    # path('category/', views.ManageCategoryPage, name='ManageCategoryPage'),
    path('', views.ListProductViewPage, name='ListProductViewPage'),
    path('<str:slug>/', views.ViewProductPage, name='ViewProductPage'),
    path('category/<str:category_url>/', views.CategoryProductPage, name='CategoryProductPage'),
    path('checkout/<str:slug>/', views.CheckOutPage, name='CheckOutPage'),


]