from rest_framework import serializers
from product.models import (Product,
                            Category,
                            ProductImage,
                            )
from auth_profile.models import Seller

class CategorySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'description',
        ]
        
class ProductImageSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    
    class Meta:
        model = ProductImage
        fields = [
            'id',
            'title',
            'image',
            'product',
        ]
    
class ProductSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    seller = serializers.PrimaryKeyRelatedField(queryset=Seller.objects.all())
    
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            'thumbnail',
            'seller',
        ]