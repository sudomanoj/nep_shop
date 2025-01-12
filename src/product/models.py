from django.db import models
from common.models import TimeStampMixin
from uuid import uuid4
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
    
    description = models.TextField(
        verbose_name='description'
        )
    
    product = models.ManyToManyField(
        'Product',
        related_name='categories',
        verbose_name='product'
        )
    
    def __str__(self):
        return self.name
    
class Rating(TimeStampMixin):
    
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
        )
    
    rating = models.PositiveIntegerField(
        verbose_name='rating'
        )
    
    review = models.TextField(
        verbose_name='review'
        )
    
    buyer = models.ForeignKey(
        Buyer,
        on_delete=models.CASCADE,
        related_name='ratings',
        verbose_name='buyer'
        )
    
    def __str__(self):
        return str(self.rating)
    
    def get_average_rating(self):
        ratings = Rating.objects.filter(product=self.product)
        total = 0
        for rating in ratings:
            total += rating.rating
        return total / len(ratings)
    
    
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
    
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='price'
        )
    
    stock = models.PositiveIntegerField(
        verbose_name='stock'
        )
    
    thumbnail = models.ImageField(
        upload_to='product/thumbnails',
        verbose_name='thumbnail'
        )
    
    seller = models.ForeignKey(
        Seller,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='seller'
        )
    
    def __str__(self):
        return self.name
    
    
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
        upload_to='product/images',
        verbose_name='image'
        )
    
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='product'
        )
    
    def __str__(self):
        return self.title or self.product.name
    
    