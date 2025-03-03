from rest_framework import serializers
from product.models import (Product,
                            Category,
                            ProductImage,
                            )
from auth_profile.models import Seller
from auth_profile.serializers import SellerSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'description',
        ]
        
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = [
            'id',
            'title',
            'image',
            'product',
        ]
    
class ProductAddSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    seller = serializers.PrimaryKeyRelatedField(queryset=Seller.objects.all())
    images = serializers.PrimaryKeyRelatedField(many=True, queryset=ProductImage.objects.all())
    category = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())
    
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            'thumbnail',
            'seller',
            'images',
            'category',
        ]
        
class ProductSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    seller = SellerSerializer()
    images = ProductImageSerializer(many=True)
    category = CategorySerializer(many=True)
    
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            'stock',
            'thumbnail',
            'seller',
            'images',
            'category',
        ]