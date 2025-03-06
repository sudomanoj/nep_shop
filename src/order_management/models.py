from django.db import models
from common.mixins import TimeStampMixin
from auth_profile.models import Buyer
from product.models import Product

from uuid import uuid4
import datetime
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.

class Coupon(TimeStampMixin):
    """
    Database model to store coupon related data
    """
    COUPON_TYPE = (
        ('percentage', 'Percentage'),
        ('fixed', 'Fixed'),
    )
    
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    
    name = models.CharField(
        max_length=255
    )
    
    code = models.CharField(
        validators=[MinLengthValidator(5), MaxLengthValidator(5)],
        max_length=5,
        unique=True
    )
    
    coupon_type = models.CharField(
        max_length=10,
        choices=COUPON_TYPE,
        default='fixed'
    )
    
    discount_value = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    
    max_discount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    
    min_purchase = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    
    valid_from = models.DateTimeField()
    
    valid_to = models.DateTimeField()
    
    is_active = models.BooleanField(
        default=True
    )
    
    def __str__(self):
        return str(self.name)
    
    def is_valid(self):
        _now = datetime.now()
        return self.valid_from <= _now and self.valid_to >= _now
    
    class Meta:
        unique_together = ['code', 'is_active']
 

class CustomerCoupon(TimeStampMixin):
    """
    Database model to store customer coupon related data
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )   
    
    customer = models.ForeignKey(
        Buyer,
        on_delete=models.CASCADE,
        related_name='%(class)s_customer'
    )
    
    coupon = models.ForeignKey(
        Coupon,
        on_delete=models.CASCADE,
        related_name='%(class)s_coupon'
    )
    
    def __str__(self):
        return str(self.customer.get_full_name()) + ' - ' + str(self.coupon.name)
    
    class Meta:
        unique_together = ['customer', 'coupon']    
        
        

class Cart(TimeStampMixin):
    """
    Database model to store cart related data
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid4
    )
    
    customer = models.ForeignKey(
        Buyer,
        on_delete=models.SET_NULL,
        null=True,
        related_name='%(class)s_customer'
    )
    

    def __str__(self):
        return str(self.customer.get_full_name()) 
    
    
class CartItem(TimeStampMixin):
    """
    Database model to store cart item related data
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid4
    )
    
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='%(class)s_cart'
    )
    
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='%(class)s_product'
    )
    
    quantity = models.PositiveIntegerField(
        default=1
    )
    
    def __str__(self):
        return str(self.product.name) + ' - ' + str(self.quantity)
    
    class Meta:
        unique_together = ['cart', 'product']
        
        
class Order(TimeStampMixin):
    """
    Database model to store order related data
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid4
    )
    
    customer = models.ForeignKey(
        Buyer,
        on_delete=models.SET_NULL,
        null=True,
        related_name='%(class)s_customer'
    )
    
    cart = models.ForeignKey(
        Cart,
        on_delete=models.SET_NULL,
        null=True,
        related_name='%(class)s_cart'
    )
    
    coupon = models.ForeignKey(
        Coupon,
        on_delete=models.SET_NULL,
        null=True,
        related_name='%(class)s_coupon'
    )
    
    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    
    discount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    
    def calculate_total(self):
        """
        Calculate the total order amount after applying the coupon discount.
        """
        self.subtotal = sum(item.product.price * item.quantity for item in self.orderitem_order.all())

        # Initialize discount
        self.discount = 0

        # Apply coupon discount if available
        if self.coupon:
            if self.coupon.coupon_type == 'percentage':
                self.discount = (self.subtotal * self.coupon.discount_value) / 100
            else:
                self.discount = self.coupon.discount_value
                
            # Ensure discount does not exceed max limit
            self.discount = min(self.discount, self.coupon.max_discount)
        self.total = self.subtotal - self.discount
       
        
    def save(self, *args, **kwargs):
        """
        Override the save method to calculate the total order amount before saving.
        """
        self.calculate_total()
        super().save(*args, **kwargs)

    
    def __str__(self):
        return str(self.customer.get_full_name()) + ' - ' + str(self.total)
    
    class Meta:
        unique_together = ['customer', 'cart']
        
class OrderItem(TimeStampMixin):
    """
    Database model to store order item related data
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid4
    )
    
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )
    
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='%(class)s_product'
    )
    
    quantity = models.PositiveIntegerField(
        default=1
    )
    
    def __str__(self):
        return str(self.product.name) + ' - ' + str(self.quantity)
    
    class Meta:
        unique_together = ['order', 'product']