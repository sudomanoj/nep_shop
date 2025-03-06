from rest_framework import serializers
from order_management.models import Order, OrderItem, Coupon, CustomerCoupon
from product.models import Product
from product.serializers import ProductSerializer


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = [
            'id',
            'code',
            'discount',
            'valid_from',
            'valid_to',
            'active',
        ]
        
    def validate_valid_from(self, valid_from):
        if valid_from >= self.instance.valid_to:
            raise serializers.ValidationError("valid_from date must be before valid_to date")
        return valid_from
    

class OrderItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderItem
        fields = [
            'id',
            'order',
            'product',
            'quantity',
        ]
        



class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    coupon = serializers.CharField(write_only=True, required=False) 
    
    class Meta:
        model = Order
        fields = [
            'id',
            'customer',
            'cart',
            'items',
            'coupon',
        ]
        
    def validate_coupon(self, coupon):
        customer = self.instance.customer
        if not Coupon.objects.filter(code=coupon).exists():
            raise serializers.ValidationError("Coupon is expired or does not exist")
        
        if CustomerCoupon.objects.filter(customer=customer, coupon__code=coupon).exists():
            raise serializers.ValidationError("Coupon already used")
        
        return coupon
    
    def create(self, validated_data):
        items = validated_data.pop('items')
        coupon = validated_data.pop('coupon', None)
        
        order = Order.objects.create(**validated_data)
        
        for item in items:
            OrderItem.objects.create(order=order, **item)
        
        if coupon:
            coupon_obj = Coupon.objects.get(code=coupon)
            CustomerCoupon.objects.create(customer=order.customer, coupon=coupon_obj)
        
        return order
        
        
        