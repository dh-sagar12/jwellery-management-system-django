from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from product.models import OrderDetailModel, ProductModel
from . import models

# Create your views here.


def home(request):

    banner_images=  models.BannerImagesModel.objects.filter(is_active =  True)
    main_feature_item  =  models.FeatureProductModel.objects.get(is_main =  True, is_active  =  True)
    other_feature_item =  models.FeatureProductModel.objects.filter(is_active  = True, is_main  =  False)
    products =  ProductModel.objects.all().order_by('id')[:5]
    data = {
        'banner_images': banner_images, 
        'main_feature_item': main_feature_item, 
        'other_feature_item': other_feature_item, 
        'products': products
    }

    return render(request, 'home/index.html', data)


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)



@login_required(login_url='/auth/login')
def MyPurchases(request):
    orders =  OrderDetailModel.objects.filter(ordered_by =  request.user).order_by('id')
    context = {
        'pruchases': orders
    }
    return render(request, 'home/mypurchases.html', context)
