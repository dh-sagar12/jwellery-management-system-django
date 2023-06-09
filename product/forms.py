# >>> class ArticleForm(ModelForm):
# ...     class Meta:
# ...         model = Article
# ...         fields = ["pub_date", "headline", "content", "reporter"]



from django import forms
from product.models import InventoryModel, OrderDetailModel, ProductCategoryModel, ProductModel


class ProductCatgoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super(ProductCatgoryForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'block  px-4 py-2 mt-2 text-purple-600 bg-white border rounded-md focus:border-purple-400 focus:ring-purple-300 focus:outline-none focus:ring focus:ring-opacity-40'
    
    class Meta:
        model = ProductCategoryModel
        fields = ("category_name", "category_url_name" ,  "is_active")



class CustomManyToManyFormField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, category):
         return "%s" % category.category_name

        
class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super(ProductForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'block  px-4 py-2 mt-2 text-purple-600 bg-white border rounded-md focus:border-purple-400 focus:ring-purple-300 focus:outline-none focus:ring focus:ring-opacity-40'
    
    
    class Meta:
        model =  ProductModel
        fields = '__all__'
        

    categories =  CustomManyToManyFormField(
        queryset=ProductCategoryModel.objects.filter(is_active  =  True), 
        widget=forms.CheckboxSelectMultiple

    )


class InventoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super(InventoryForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'block  px-4 py-2 mt-2 text-purple-600 bg-white border rounded-md focus:border-purple-400 focus:ring-purple-300 focus:outline-none focus:ring focus:ring-opacity-40'
    
    class Meta:
        model = InventoryModel
        fields = ("product_id", 'quantity', 'rate')


class OrderDetailForm(forms.ModelForm):
     
    def __init__(self, *args, **kwargs):
            super(OrderDetailForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'block  px-4 py-2 mt-2 text-purple-600 bg-white border rounded-md focus:border-purple-400 focus:ring-purple-300 focus:outline-none focus:ring focus:ring-opacity-40 w-full'

    # product_id  =  forms.CharField(required=False)
    total_price  =  forms.CharField(required=False)
    order_staus  =  forms.CharField(required=False)
    payment_completed  =  forms.CharField(required=False)

    class Meta:
        model  =  OrderDetailModel
        fields  =  (  'quantity',  'customer_name', 'primary_delivery_address', 'secondary_delivery_address', 'postal_code', 'city', 'order_staus', 'payment_completed'
        )
        widgets= {
            'customer_name': forms.TextInput(attrs= {'placeholder': 'Enter Your Name'}),
            'quantity': forms.NumberInput(attrs={'placeholder': 'Order Quantity'} ),
            'primary_delivery_address': forms.TextInput(attrs={'placeholder': 'Address Line 1'} ),
            'secondary_delivery_address': forms.TextInput(attrs={'placeholder': 'Address Line 2'} ),
            'postal_code': forms.TextInput(attrs={'placeholder': 'Postal Code'} ),
            'city': forms.TextInput(attrs={'placeholder': 'City'} )
        }

