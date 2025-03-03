from django.db import models
from common.models import TimeStampMixin
from nep_shop.utils import unique_slugify, get_image_upload_path
from uuid import uuid4
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from auth_profile.models import (
    Buyer,
    Seller
)
# Create your models here.

class Category(TimeStampMixin):
    
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
        )
    
    name = models.CharField(
        max_length=255,
        verbose_name='name'
        )
    
    slug = models.SlugField(
        max_length=255,
        verbose_name='slug',
        unique=True, 
        editable=False
        )
    
    description = models.TextField(
        verbose_name='description'
        )
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.name))
        super().save(*args, **kwargs)
    
class Rating(TimeStampMixin):
    
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
        )
    
    rating = models.PositiveIntegerField(
        verbose_name='rating',
        validators=[MinValueValidator(1), MaxValueValidator(5)]
        )
    
    review = models.TextField(
        verbose_name='review'
        )
    
    buyer = models.ForeignKey(
        Buyer,
        on_delete=models.CASCADE,
        related_name='%(class)s_buyer',
        verbose_name='buyer'
        )
    
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='%(class)s_product',
        verbose_name='product'
        )
    
    def __str__(self):
        return str(self.rating)
    
    class Meta:
        unique_together = ['buyer', 'product']
    
    
class Product(TimeStampMixin):
    
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
        )
    
    name = models.CharField(
        max_length=255,
        verbose_name='name'
        )
    
    description = models.TextField(
        verbose_name='description'
        )
    
    slug = models.SlugField(
        max_length=255,
        verbose_name='slug',
        unique=True,
        editable=False
        )
    
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='price'
        )
    
    stock = models.PositiveIntegerField(
        verbose_name='stock',
        default=0
        )
    
    thumbnail = models.ImageField(
        upload_to=get_image_upload_path,
        verbose_name='thumbnail'
        )
    
    seller = models.ForeignKey(
        Seller,
        on_delete=models.CASCADE,
        related_name='%(class)s_seller',
        verbose_name='seller'
        )
    
    category = models.ManyToManyField(
        Category,
        related_name='%(class)s_category',
        verbose_name='category'
    )
    
    def __str__(self):
        return self.name
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.name))
        super().save(*args, **kwargs)
    
    
class ProductImage(TimeStampMixin):
    
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
        )
    
    title = models.CharField(
        max_length=255,
        verbose_name='title',
        blank=True, 
        null=True
        )
    
    image = models.ImageField(
        upload_to=get_image_upload_path,
        verbose_name='image'
        )
    
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='%(class)s_product',
        verbose_name='product'
        )
    
    def __str__(self):
        return self.title or self.product.name
    
    