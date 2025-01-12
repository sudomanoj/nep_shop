from rest_framework import serializers
from product.models import (Product,
                            Category,
                            ProductImage,
                            )

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
    
    class Meta:
        model = ProductImage
        fields = [
            'id',
            'image',
            'product',
        ]
    
class ProductSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    images = ProductImageSerializer(many=True)
    
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            'category',
            'images',
        ]
        
    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        product = Product.objects.create(**validated_data)
        for image_data in images_data.values():
            ProductImage.objects.create(product=product, image=image_data)
        return product