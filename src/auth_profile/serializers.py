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
    # id = serializers.UUIDField(read_only=True)
    user_info = UserCreateSerializer(read_only=True)
    # store = serializers.PrimaryKeyRelatedField(queryset=Store.objects.all())
    
    class Meta:
        model = Seller
        fields = [
            'id',
            'first_name',
            'last_name',
            'user',
            'store',
            'user_info',
        ]
        
    # def validate_user(self, user_id):
    #     """
    #     Validate that the user exists and return the user instance.
    #     """
    #     try:
    #         user = User.objects.get(id=user_id)
    #         return user
    #     except User.DoesNotExist:
    #         raise serializers.ValidationError("User does not exist")

    # def validate_store(self, store_id):
    #     """
    #     Validate that the store exists and return the store instance.
    #     """
    #     try:
    #         store = Store.objects.get(id=store_id)
    #         return store
    #     except Store.DoesNotExist:
    #         raise serializers.ValidationError("Store does not exist")
    
    
    # def create(self, validated_data):
    #     # Directly use the validated user and store instances
    #     user = validated_data.pop('user')
    #     store = validated_data.pop('store')
    #     seller = Seller.objects.create(user=user, store=store, **validated_data)
    #     return seller