from rest_framework import serializers
from product.models import (Product,
                            Category,
                            ProductImage,
                            Rating,
                            )
from auth_profile.models import Buyer
from auth_profile.models import Seller
from auth_profile.serializers import SellerSerializer
from django.db.models import Avg

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
    productimage_product = ProductImageSerializer(many=True)
    category = CategorySerializer(many=True)
    average_rating = serializers.SerializerMethodField()
    
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
            'productimage_product',
            'category',
            'average_rating',
        ]
        
    def get_average_rating(self, obj):
        # Calculate the average rating for the product
        average_rating = Rating.objects.filter(product=obj).aggregate(Avg('rating'))['rating__avg']
        return average_rating if average_rating is not None else 0
    
    
class RatingSerializer(serializers.ModelSerializer):
    buyer = serializers.PrimaryKeyRelatedField(queryset=Buyer.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    
    class Meta:
        model = Rating
        fields = [
            'id',
            'rating',
            'buyer',
            'product',
        ]
        
    def create(self, validated_data):
        # Check if the buyer has already rated the product and buyer is the same
        user = self.context['request'].user
        
        if not hasattr(user, 'buyer'):
            raise serializers.ValidationError('You are not a buyer')
        validated_data['buyer'] = user.buyer
        
        if Rating.objects.filter(buyer=validated_data['buyer'], product=validated_data['product']).exists():
            raise serializers.ValidationError('You have already rated this product')
        return super().create(validated_data)