from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from home.forms import BannerImagesForm, FeatureProductForm

from home.models import BannerImagesModel, FeatureProductModel


# Create your views here.


@login_required(login_url='/auth/login')
def AdminHomePage(request):
    if request.user.is_admin or  request.user.is_admin:  
        return render(request, 'siteadmin/home.html')
    else: 
        return render(request, '404.html')


@login_required(login_url='/auth/login')
def SettingPage(request):
    if request.user.is_admin or request.user.is_admin:  
        return render(request, 'siteadmin/setting.html')
    else: 
        return render(request, '404.html')






# Feature Product views start form here 

@login_required(login_url='/auth/login')
def ManageFeatureProductPage(request):
    if request.user.is_admin or request.user.is_admin:  
        feature_product_data  =  FeatureProductModel.objects.all().order_by('id')
        context =  {
            'feature_product_data': feature_product_data, 
        }
        return render(request, 'siteadmin/feature_product.html', context=context)
    else: 
        return render(request, '404.html')
    

@login_required(login_url='/auth/login')
def AddFeatureProductPage(request):
    if request.user.is_admin or request.user.is_admin:  
        form =  FeatureProductForm(request.POST  or None)
        if form.is_valid():
            newform  =  form.save(commit=False)
            newform.created_by  = request.user 
            newform.save()
            return redirect('ManageFeatureProductPage')
        else:
            data  =  {
                'action_url': 'AddFeatureProductPage',
                'form_title': 'Add Feature Products', 
                'form': form
            }

            return render(request, 'siteadmin/addform.html', data)
    else: 
        return render(request, '404.html')
     

    
@login_required(login_url='/auth/login')
def EditFeatureProduct(request, id):
    if request.user.is_admin or request.user.is_admin:  
        feature_product  =  get_object_or_404(FeatureProductModel, id=id )
        
        if request.method == 'GET':
            context = {
                'form': FeatureProductForm(instance=feature_product),
                'id': id,
                'form_title': 'Edit Feature Product',
                
                }
            return render(request,'siteadmin/addform.html',context)
    
        elif request.method  == 'POST':
            form =  FeatureProductForm(request.POST , request.FILES,  instance=feature_product)
            if form.is_valid():
                form.save()
                return redirect('ManageFeatureProductPage')
            else:
                context = {
                'form': FeatureProductForm(instance=feature_product),
                'id': id,
                'form_title': 'Edit Feature Product',
                
                }
            return render(request,'siteadmin/addform.html',context)
    else: 
        return render(request, '404.html')    





# Banner Image  Product views start form here 

@login_required(login_url='/auth/login')
def ManageBannerImagesPage(request):
    if request.user.is_admin or request.user.is_admin:  
        banners_data  =  BannerImagesModel.objects.all().order_by('id')
        context =  {
            'banners_data': banners_data, 
        }
        return render(request, 'siteadmin/banner.html', context=context)
    else: 
        return render(request, '404.html')
    

@login_required(login_url='/auth/login')
def AddBannerImagesPage(request):
    if request.user.is_admin or request.user.is_admin:  
        form =  BannerImagesForm(request.POST  or None)
        if form.is_valid():
            newform  =  form.save(commit=False)
            newform.created_by  = request.user 
            newform.save()
            return redirect('ManageBannerImagesPage')
        else:
            data  =  {
                'action_url': 'AddBannerImagesPage',
                'form_title': 'Add Feature Products', 
                'form': form
            }

            return render(request, 'siteadmin/addform.html', data)
    else: 
        return render(request, '404.html')
     

    
@login_required(login_url='/auth/login')
def EditBannerImages(request, id):
    if request.user.is_admin or request.user.is_admin:  
        banner_image  =  get_object_or_404(BannerImagesModel, id=id )
        
        if request.method == 'GET':
            context = {
                'form': BannerImagesForm(instance=banner_image),
                'id': id,
                'form_title': 'Edit Banner Images',
                
                }
            return render(request,'siteadmin/addform.html',context)
    
        elif request.method  == 'POST':
            form =  BannerImagesForm(request.POST , request.FILES,  instance=banner_image)
            if form.is_valid():
                form.save()
                return redirect('ManageFeatureProductPage')
            else:
                context = {
                'form': BannerImagesForm(instance=banner_image),
                'id': id,
                'form_title': 'Edit Banner Images',
                
                }
            return render(request,'siteadmin/addform.html',context)
    else: 
        return render(request, '404.html')    
