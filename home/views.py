from django.shortcuts import render
from . import models

# Create your views here.


def home(request):

    banner_images=  models.BannerImagesModel.objects.filter(is_active =  True)
    main_feature_item  =  models.FeatureProductModel.objects.get(is_main =  True, is_active  =  True)
    other_feature_item =  models.FeatureProductModel.objects.filter(is_active  = True, is_main  =  False)
    data = {
        'banner_images': banner_images, 
        'main_feature_item': main_feature_item, 
        'other_feature_item': other_feature_item
    }

    return render(request, 'home/index.html', data)