from django.db import connection
from django.shortcuts import get_object_or_404, redirect, render

from product.models import InventoryModel, OrderDetailModel, ProductCategoryModel, ProductModel
from .forms import InventoryForm, OrderDetailForm, ProductCatgoryForm, ProductForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator 
from django.db.models import Sum
from django.db.models.functions import Coalesce



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
    


def RemainingInventory(product_id):
    with connection.cursor() as cursor:
        cursor.execute('''
            WITH inv as (
	            SELECT COALESCE(SUM(quantity), 0) stock_qty FROM inventory 
	            WHERE product_id =  %s
                    ),
            sold as (
                SELECT COALESCE(SUM(quantity), 0) sold_qty FROM order_details 
                WHERE product_id =  %s
            )
            SELECT inv.stock_qty::numeric  -  sold.sold_qty::numeric from inv, sold
        ''', [product_id])
        row = cursor.fetchone()
        remaining_stock_count = row[0] if row[0] is not None else 0
    
        return remaining_stock_count

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
        inventory_data  =  InventoryModel.objects.all().order_by('id')
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


def ListProductViewPage(request):

    page = request.GET.get('page')
    from_price =  request.GET.get('from_price')
    to_price =  request.GET.get('to_price')
    purity =  request.GET.get('purity')
    product_instance  =  ProductModel.objects.filter()
    if from_price:
        product_instance  =  product_instance.filter(price__gte =  from_price)

    if to_price :
        product_instance  =  product_instance.filter(price__lte =  to_price)
    
    if purity: 
        product_instance  =  product_instance.filter(purity= purity)

    all_products  =  Paginator(product_instance, 12)
    try:
        products =  all_products.page(page)
    except PageNotAnInteger:
        products =  all_products.page(1)
    except EmptyPage:
        products  -  all_products.page(all_products.num_pages)

    context =  {
        'products': products
    }
    return render(request, 'products/product.html', context)



def ViewProductPage(request, slug):
    product  =  get_object_or_404(ProductModel, slug=slug )
    # remaining_stock =  RemainingInventory(product_id=product.id)              

    context =  {
        'product': product, 
        # 'remaining_stock': remaining_stock
    }
    return render(request, 'products/viewproduct.html', context)



def CategoryProductPage(request, category_url):
    from_price =  request.GET.get('from_price')
    to_price =  request.GET.get('to_price')
    purity =  request.GET.get('purity')
    page =  request.GET.get('page')


    try:
        category = get_object_or_404(ProductCategoryModel, category_url_name=category_url)
    except Exception as e:
        return render(request, '404.html')
    
    product_instance  =  category.products.all()

    if from_price:
        product_instance  =  product_instance.filter(price__gte =  from_price)

    if to_price :
        product_instance  =  product_instance.filter(price__lte =  to_price)
    
    if purity: 
        product_instance  =  product_instance.filter(purity= purity)

    all_products = Paginator(product_instance, 12)
    try:
        products =  all_products.page(page)
    except PageNotAnInteger:
        products =  all_products.page(1)
    except EmptyPage:
        products  -  all_products.page(all_products.num_pages)

    context = {'category': category, 'products': products}
    return render(request, 'products/product.html', context)


@login_required(login_url='/auth/login')
def CheckOutPage(request, slug):
    try:
        product =  get_object_or_404(ProductModel, slug=slug)
        print(product.id)
    except Exception as e:
        return render(request, '404.html')

    form  = OrderDetailForm(request.POST or None)
    # remaining_stock  =  RemainingInventory(product_id=product.id)
    if form.is_valid():
        newform =  form.save(commit=False)
        newform.ordered_by =  request.user
        newform.total_price =  newform.quantity * product.price
        newform.product_id =  product
        newform.save()
        # return render(request, 'products/ordersucess.html')
        return redirect('home')
    else:
        data  =  {
                'product': product, 
                'form': form
                }

        return render(request, 'products/checkout.html', data)
        


