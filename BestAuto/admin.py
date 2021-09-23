from django.contrib import admin
from .models import Products
from .models import Contact, ProductsImage

# Register your models here.
admin.site.register(Contact)

#admin.site.register(Products)
#admin.site.register(ProductsImage)

class ProductsImageAdmin(admin.StackedInline):
    model = ProductsImage

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    inlines = [ProductsImageAdmin]

    class Meta:
        model = Products

@admin.register(ProductsImage)
class ProductsImageAdmin(admin.ModelAdmin):
    pass
# Register your models here.
