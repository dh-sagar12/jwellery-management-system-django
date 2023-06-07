from django.shortcuts import get_object_or_404, redirect, render

from product.models import InventoryModel, ProductCategoryModel, ProductModel
from .forms import InventoryForm, ProductCatgoryForm, ProductForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/auth/login')
def ManageCategoryPage(request):
    if request.user.is_admin or request.user.is_admin:  
        category_data  =  ProductCategoryModel.objects.filter(is_active  =  True)
        context =  {
            'category_data': category_data, 
            'edit_view': 'EditCategory'
        }
        return render(request, 'siteadmin/category.html', context=context)
    else: 
        return render(request, '404.html')
    

@login_required(login_url='/auth/login')
def AddCategoryPage(request):
    if request.user.is_admin or request.user.is_admin:  
        form =  ProductCatgoryForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('ManageCategoryPage')
        else:
            data  =  {
                'action_url': 'AddCategoryPage',
                'form_title': 'Add Category', 
                'form': form
            }

            return render(request, 'siteadmin/addform.html', data)
    else: 
        return render(request, '404.html')
    

@login_required(login_url='/auth/login')
def EditCategory(request, id):
    if request.user.is_admin or request.user.is_admin:  
        category  =  get_object_or_404(ProductCategoryModel, id=id )
        
        if request.method == 'GET':
            context = {
                'form': ProductCatgoryForm(instance=category),
                'id': id,
                'form_title': 'Edit Category',
                
                }
            return render(request,'siteadmin/addform.html',context)
    
        elif request.method  == 'POST':
            form =  ProductCatgoryForm(request.POST , instance=category)
            if form.is_valid():
                form.save()
                return redirect('ManageCategoryPage')
            else:
                context = {
                'form': ProductCatgoryForm(instance=category),
                'id': id,
                'form_title': 'Edit Category',
                
                }
            return render(request,'siteadmin/addform.html',context)
    else: 
        return render(request, '404.html')



# product related view start form here 
@login_required(login_url='/auth/login')
def ManageProductPage(request):
    if request.user.is_admin or request.user.is_admin:  
        product_data  =  ProductModel.objects.filter(is_active  =  True)
        context =  {
            'product_data': product_data, 
        }
        return render(request, 'siteadmin/product.html', context=context)
    else: 
        return render(request, '404.html')

@login_required(login_url='/auth/login')
def AddProductPage(request):
    if request.user.is_admin or request.user.is_admin:  
        form =  ProductForm(request.POST or None , request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('ManageProductPage')
        else:
            data  =  {
                'action_url': 'AddProductPage',
                'form_title': 'Add Product', 
                'form': form
            }

            return render(request, 'siteadmin/addform.html', data)
    else: 
        return render(request, '404.html')
     
@login_required(login_url='/auth/login')
def EditProduct(request, id):
    if request.user.is_admin or request.user.is_admin:  
        product  =  get_object_or_404(ProductModel, id=id )
        
        if request.method == 'GET':
            context = {
                'form': ProductForm(instance=product),
                'id': id,
                'form_title': 'Edit Product',
                
                }
            return render(request,'siteadmin/addform.html',context)
    
        elif request.method  == 'POST':
            form =  ProductForm(request.POST , request.FILES,  instance=product)
            if form.is_valid():
                form.save()
                return redirect('ManageProductPage')
            else:
                context = {
                'form': ProductForm(instance=product),
                'id': id,
                'form_title': 'Edit Product',
                
                }
            return render(request,'siteadmin/addform.html',context)
    else: 
        return render(request, '404.html')    




# inventory views start form here 

@login_required(login_url='/auth/login')
def ManageInventoryPage(request):
    if request.user.is_admin or request.user.is_admin:  
        inventory_data  =  InventoryModel.objects.all()
        context =  {
            'inventory_data': inventory_data, 
        }
        return render(request, 'siteadmin/inventory.html', context=context)
    else: 
        return render(request, '404.html')
    

@login_required(login_url='/auth/login')
def AddInventoryPage(request):
    if request.user.is_admin or request.user.is_admin:  
        form =  InventoryForm(request.POST  or None)
        if form.is_valid():
            newform  =  form.save(commit=False)
            newform.created_by  = request.user 
            newform.save()
            return redirect('ManageInventoryPage')
        else:
            data  =  {
                'action_url': 'AddInventoryPage',
                'form_title': 'Add Inventory', 
                'form': form
            }

            return render(request, 'siteadmin/addform.html', data)
    else: 
        return render(request, '404.html')
     