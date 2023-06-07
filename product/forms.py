# >>> class ArticleForm(ModelForm):
# ...     class Meta:
# ...         model = Article
# ...         fields = ["pub_date", "headline", "content", "reporter"]



from django import forms
from product.models import InventoryModel, ProductCategoryModel, ProductModel


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
