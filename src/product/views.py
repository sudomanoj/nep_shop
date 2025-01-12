from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from product.models import (Product,
                            Category,
                            ProductImage,
                            )
from product.serializers import (CategorySerializer,
                                 ProductSerializer,
                                 ProductImageSerializer,
                                 )

# Create your views here.

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]