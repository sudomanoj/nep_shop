from django.contrib import admin
from product.models import (Product,
                            Category,
                            ProductImage,
                            )
from django.utils.html import format_html

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
    ]
    
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ['title', 'image', 'product_image']
    readonly_fields = ['product_image']
    
    def product_image(self, obj):
        if obj.image:   
            return format_html('<img src="{}" width="100" />'.format(obj.image.url))
        return 'No Image'
    product_image.short_description = 'Preview Image'
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'price',
    ]
    inlines = [ProductImageInline]