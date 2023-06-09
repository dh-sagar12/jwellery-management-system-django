from home.models import BannerImagesModel, FeatureProductModel
from django import forms



class FeatureProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super(FeatureProductForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'block  px-4 py-2 mt-2 text-purple-600 bg-white border rounded-md focus:border-purple-400 focus:ring-purple-300 focus:outline-none focus:ring focus:ring-opacity-40'


    class Meta:
        model  =  FeatureProductModel
        fields = '__all__'

        
class BannerImagesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super(BannerImagesForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'block  px-4 py-2 mt-2 text-purple-600 bg-white border rounded-md focus:border-purple-400 focus:ring-purple-300 focus:outline-none focus:ring focus:ring-opacity-40'


    class Meta:
        model  =  BannerImagesModel
        fields = '__all__'