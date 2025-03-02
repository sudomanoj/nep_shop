from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from auth_profile.models import (
    User,
    Seller,
    Buyer,
    Store,
)
from .forms import (
    CustomAdminAuthenticationForm,
)
from nep_shop.mixins import BaseAdmin
from django.contrib.admin import AdminSite
# Register your models here.


class CustomAdminSite(AdminSite):
    site_header = 'Nep Shop Admin'
    site_title = 'Nep Shop Admin'
    index_title = 'Nep Shop Admin'
    login_form = CustomAdminAuthenticationForm  # Use custom form

custom_admin_site = CustomAdminSite(name="custom_admin")
admin.site = custom_admin_site   

@admin.register(User, site=custom_admin_site)
class UserAdmin(DjangoUserAdmin):
    list_display = ['email', 'phone_number', 'is_active', 'is_staff', 'date_joined']
    search_fields = ['email', 'phone_number']
    list_filter = ['is_active', 'is_staff']
    readonly_fields = ['date_joined']
    fieldsets = (
        ('General', {'fields': ('email', 'phone_number', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
    )
    add_fieldsets = (
        ('General', {
            'classes': ('wide',),
            'fields': ('email', 'phone_number', 'password1', 'password2')}
        ),
        ('Permissions', {
            'classes': ('wide',),
            'fields': ('is_active', 'is_staff')}
        )
    )
    ordering = ['email']
    filter_horizontal = ()
 
@admin.register(Seller, site=custom_admin_site)
class SellerAdmin(BaseAdmin):
    list_display = ['first_name', 'last_name', 'user', 'store', 'created_at', 'updated_at']
    fieldsets = (
        ('General', {'fields': ('first_name', 'last_name')}),
        ('User', {'fields': ('user',)}),
        ('Store', {'fields': ('store',)}),
    )
    
@admin.register(Buyer, site=custom_admin_site)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'updated_at']
    search_fields = ['user']
    list_filter = ['created_at', 'updated_at']
    
@admin.register(Store, site=custom_admin_site)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'rating']
    search_fields = ['name', 'description']
    list_filter = ['rating']