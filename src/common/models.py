from django.db import models

# Create your models here.

class TimeStampMixin(models.Model):
    
    created_at = models.DateTimeField(
        auto_now_add=True
        )
    
    updated_at = models.DateTimeField(
        auto_now=True
        )

    class Meta:
        abstract = True
        
class UserStampMixin(models.Model):
    
    created_by = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='created_%(class)s',
        null=True,
        blank=True
        )
    
    updated_by = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='updated_%(class)s',
        null=True,
        blank=True
        )
    
    class Meta:
        abstract = True
        