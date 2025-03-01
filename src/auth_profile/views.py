from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateAPIView,
    )
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import ValidationError, MethodNotAllowed
from auth_profile.serializers import (
    UserListSerializer,
    UserCreateSerializer,
    UserLoginSerializer,
    StoreSerializer,
    SellerSerializer,
    )
from auth_profile.models import (
    User,
    Store,
    Seller,
    )
from . import docs
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.contrib.auth import authenticate

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework_simplejwt.tokens import RefreshToken


class UserViewSet(ViewSet):
    permission_classes = [AllowAny,]
    
    @docs.CREATEUSER
    def create(self, request):  # Handles user creation
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
    
    @docs.LISTUSER
    def list(self, request): # Handles user listing
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)
    
    @docs.RETRIEVEUSER
    def retrieve(self, request, pk=None):  # Handles user retrieval
        user = User.objects.get(id=pk)
        serializer = UserCreateSerializer(user)
        return Response(serializer.data)

    @docs.USERLOGIN
    @action(detail=False, methods=['post'])
    def login(self, request):  # Handles user login
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user is None:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        refresh = RefreshToken.for_user(user)
        return Response({
            "message": "User Logged In successfully!",
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        }, status=status.HTTP_200_OK)


class StoreViewSet(ModelViewSet):
    """ViewSet for managing store operations."""
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    @docs.STORELIST
    def list(self, request, *args, **kwargs):
        """Handles store listing"""
        return super().list(request, *args, **kwargs)
    
    @docs.STORECREATE
    def create(self, request, *args, **kwargs):
        """Handles store creation"""
        return super().create(request, *args, **kwargs)

    @docs.STOREUPDATE
    def update(self, request, *args, **kwargs):
        """Handles complete store update"""
        response = super().update(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_204_NO_CONTENT)

    @docs.STORERETRIEVE
    def retrieve(self, request, *args, **kwargs):
        """Handles retrieving a store by ID"""
        return super().retrieve(request, *args, **kwargs)

    @docs.swagger_auto_schema(auto_schema=None)
    def destroy(self, request, *args, **kwargs):
        """Disables store deletion"""
        raise MethodNotAllowed("DELETE method is not allowed.")

    @docs.swagger_auto_schema(auto_schema=None)
    def partial_update(self, request, *args, **kwargs):
        """Disables partial updates (PATCH)"""
        raise MethodNotAllowed("PATCH method is not allowed.")
    

class SellerViewSet(ModelViewSet):
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()
    
    # @swagger_auto_schema(request_body=SellerSerializer)
    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)
    

    

    
