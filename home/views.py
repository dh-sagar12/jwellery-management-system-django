from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from product.forms import OrderDetailForm
from product.models import OrderDetailModel, ProductModel, ProductCategoryModel
from . import models
from django.http import JsonResponse

# Create your views here.


def home(request):

    banner_images = models.BannerImagesModel.objects.filter(is_active=True)
    main_feature_item = models.FeatureProductModel.objects.get(
        is_main=True, is_active=True)
    other_feature_item = models.FeatureProductModel.objects.filter(
        is_active=True, is_main=False)
    products = ProductModel.objects.all().order_by('id')[:5]
    if request.user.is_authenticated:
        user_cart = models.MyCart.objects.filter(user_id=request.user)
        result_list = [item.product_id for item in user_cart]
    else:
        result_list = []

    data = {
        'banner_images': banner_images,
        'main_feature_item': main_feature_item,
        'other_feature_item': other_feature_item,
        'products': products, 
        'user_cart': result_list
    }

    return render(request, 'home/index.html', data)


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


@login_required(login_url='/auth/login')
def MyPurchases(request):
    orders = OrderDetailModel.objects.filter(
        ordered_by=request.user).order_by('id')
    context = {
        'pruchases': orders
    }
    return render(request, 'home/mypurchases.html', context)


@login_required(login_url='/auth/login')
def PostCartView(request, id):
    if request.method == 'POST':
        try:
            # item = get_object_or_404(models.MyCart, id=id)
            item = models.MyCart.objects.filter(
                product_id=id, user_id=request.user)
            print('ITEM', item)
            if item:
                try:
                    item.delete()
                    return JsonResponse({
                        'status': 200,
                        'message': 'Cart deleted'
                    })
                except Exception as e:
                    print(e)
            else:
                try:
                    product_instance = ProductModel.objects.get(id=id)
                    models.MyCart.objects.create(
                        user_id=request.user, product_id=product_instance)
                except Exception as e:
                    print(e)
                return JsonResponse({
                    'status': 200,
                    'message': 'Cart added'
                })
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'error_msg': e
            }, safe=False)
    else:
        return JsonResponse({
            'status': 'error',
            'error_msg': 'Method Not allowed'
        }, safe=False)


@login_required(login_url='/auth/login')
def MyCartPage(request):
    form = OrderDetailForm(request.POST or None)
    cart_items = models.MyCart.objects.filter(user_id=request.user)
    if request.method == 'POST':
        product_list = request.POST.getlist('product[]')
        print('product', product_list)
        if form.is_valid():
            data =  form.cleaned_data
            print(data)
            for item in product_list:
                print('item', item)
                temp_order =  OrderDetailModel(**data)
                product = ProductModel.objects.get(id=item)
                temp_order.ordered_by = request.user
                temp_order.total_price = temp_order.quantity * product.price
                temp_order.product_id = product
                temp_order.save()
                cart_items.delete()
            return redirect('home')


        else:
            context = {
                'cart_items': cart_items,
                'form': form
            }
            return render(request, 'home/mycart.html', context)

    context = {
        'cart_items': cart_items,
        'form': form
    }
    return render(request, 'home/mycart.html', context)


def RemoveCartItem(request, id):
    item = models.MyCart.objects.filter(id=id)
    if item:
        item.delete()
        return redirect('MyCartPage')

    else:
        return redirect('MyCartPage')
    



def AllCategoriesPage(request):
    categories  =  ProductCategoryModel.objects.filter(is_active  = True)
    context  =  {
        'categories': categories
    }
    return render(request, 'home/categories.html', context)
 
