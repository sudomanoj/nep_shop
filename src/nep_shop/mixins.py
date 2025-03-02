from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class BaseAdmin(admin.ModelAdmin):
    """
    Base Admin class for all admin classes which includes audit fields.
    """
    
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    
    def get_fieldsets(self, request, obj = ...):
        fieldsets = super().get_fieldsets(request, obj)
        if obj:
            audit_fieldsets = (
                (_('Audit Info'), {
                    'fields': ('created_at', 'updated_at'),
                    'classes': ('collapse',),
                }),
            )
            fieldsets += audit_fieldsets
        return fieldsets