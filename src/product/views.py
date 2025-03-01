from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, parsers
from product.models import (Product,
                            Category,
                            ProductImage,
                            )
from product.serializers import (CategorySerializer,
                                 ProductSerializer,
                                 ProductImageSerializer,
                                 )
from product.filters import ProductFilter
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    
    
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]
    filterset_class = ProductFilter
    parser_classes = [parsers.MultiPartParser]
    

class ProductImageViewSet(ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    # permission_classes = [IsAuthenticated]
    parser_classes = [parsers.MultiPartParser]
    
    