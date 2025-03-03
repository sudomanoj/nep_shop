from django.contrib import admin
from product.models import (Product,
                            Category,
                            ProductImage,
                            Rating,
                            )
from django.utils.html import format_html
from auth_profile.admin import custom_admin_site

# Register your models here.

@admin.register(Category, site=custom_admin_site)
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
    
@admin.register(Product, site=custom_admin_site)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'price',
    ]
    inlines = [ProductImageInline]
    

@admin.register(Rating, site=custom_admin_site)
class RatingAdmin(admin.ModelAdmin):
    list_display = [
        'rating',
        'review',
    ]
    
    list_filter = [
        'rating',
    ]
    
    search_fields = [
        'rating',
        'review',
    ]