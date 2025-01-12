from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from auth_profile.models import (
    User,
    Seller,
    Buyer,
    Store,
)
from .forms import (
    UserForm,
    UserCustomCreationForm,
)

# Register your models here.

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    list_display = ['email', 'phone_number', 'is_active', 'is_staff', 'date_joined']
    search_fields = ['email', 'phone_number']
    list_filter = ['is_active', 'is_staff']
    readonly_fields = ['date_joined']
    fieldsets = (
        (None, {'fields': ('email', 'phone_number', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone_number', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )
    ordering = ['email']
    filter_horizontal = ()
    
@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'user', 'store', 'created_at', 'updated_at']
    search_fields = ['user', 'store']
    list_filter = ['created_at', 'updated_at']
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name')}),
        ('User', {'fields': ('user',)}),
        ('Store', {'fields': ('store',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'user', 'store')}
        ),
    )
    
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'updated_at']
    search_fields = ['user']
    list_filter = ['created_at', 'updated_at']
    
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'rating']
    search_fields = ['name', 'description']
    list_filter = ['rating']