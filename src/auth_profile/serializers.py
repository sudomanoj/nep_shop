from rest_framework import serializers
from django.contrib.auth import get_user_model
from auth_profile.models import (Seller,
                                 Buyer,
                                 Store,
                                 )
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model

User = get_user_model()


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'phone_number']
        
class UserCreateSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    password = serializers.CharField(write_only=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'email', 'phone_number', 'password', 'confirm_password']
        
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        return data
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)
        return user
    

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    phone_number = serializers.CharField(required=False)
    password = serializers.CharField()
    
    def validate(self, data):
        email = data.get('email')
        phone_number = data.get('phone_number')
        if not email and not phone_number:
            raise serializers.ValidationError("Email or Phone number is required")
        return data
    

class StoreSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    
    class Meta:
        model = Store
        fields = [
            'id',
            'name',
            'description',
            'rating',
        ]
        

class SellerSerializer(serializers.ModelSerializer):
    user_id = serializers.UUIDField(write_only=True)
    store = StoreSerializer()
    
    class Meta:
        model = Seller
        fields = ['first_name', 'last_name', 'user_id', 'store']
        
    def validate_user_id(self, value):
        """
        Validate that the user exists and ensures that there is no seller 
        created yet with that user id and return the user instance.
        """
        if not User.objects.filter(id=value).exists():
            raise serializers.ValidationError("User does not exist")
        
        if Seller.objects.filter(user_id=value).exists():
            raise serializers.ValidationError("User is already a seller")
        
        return value
    
    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        store_data = validated_data.pop('store')
        user = User.objects.get(id=user_id)
        store = Store.objects.create(**store_data)
        seller = Seller.objects.create(user=user, store=store, **validated_data)
        return seller