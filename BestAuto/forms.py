from django import forms
from .models import Products, ProductsImage


class ProductsForm(forms.ModelForm):
    pname = forms.CharField(max_length=100)
    pcategory = forms.CharField(max_length=100)# Car Parts, Coins, Bones
    pprice = forms.CharField(max_length=100)
    pdescription = forms.CharField(max_length=500)
    pimage = forms.ImageField()
    pdate_posted = forms.DateTimeField()
    poffer = forms.BooleanField()
    inlines = [ProductsImage, ]


    class Meta:
        model = Products
        fields = ('pname', 'pcategory', 'pprice', 'pdescription', 'pimage', 'pdate_posted', 'poffer',)


class ProductsImageForm(forms.ModelForm):
    piimages = forms.FileField()

    class Meta:
        model = ProductsImage
        fields = ('piimages',)





