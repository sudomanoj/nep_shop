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
    images = serializers.SerializerMethodField()
    
    
    def get_images(self, obj):
        images = obj.images.all()
        return ProductImageSerializer(images, many=True).data
    
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
        ]