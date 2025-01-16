from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateAPIView,
    )
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from auth_profile.serializers import (
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
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.contrib.auth import authenticate

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework_simplejwt.tokens import RefreshToken


class UserViewSet(ViewSet):
    permission_classes = [AllowAny,]
    @swagger_auto_schema(
        request_body=UserCreateSerializer,
        responses={201: "User created successfully", 400: "Invalid data"}
    )
    
    def create(self, request):  # Handles user creation
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
    
    def list(self, request): # Handles user listing
        users = User.objects.all()
        serializer = UserCreateSerializer(users, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):  # Handles user retrieval
        user = User.objects.get(id=pk)
        serializer = UserCreateSerializer(user)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=UserLoginSerializer,
        responses={200: "Login successful", 400: "Invalid credentials"}
    )
    
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
    serializer_class = StoreSerializer
    queryset = Store.objects.all()
    

class SellerViewSet(ModelViewSet):
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()
    
    # @swagger_auto_schema(request_body=SellerSerializer)
    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)
    

    

    
