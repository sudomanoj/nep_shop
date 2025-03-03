from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, parsers
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from product.models import (
    Product,
    Category,
    ProductImage,
)
from product.serializers import (
    CategorySerializer,
    ProductSerializer,
    ProductImageSerializer,
)
from . import docs
from product.filters import ProductFilter
from drf_yasg import openapi
from rest_framework.exceptions import MethodNotAllowed


# Create your views here.

class CategoryViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    
    @docs.LISTCATEGORY
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @docs.swagger_auto_schema(auto_schema=None)
    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    @docs.CREATECATEGORY
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @docs.UPDATECATEGORY
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    
    
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]
    filterset_class = ProductFilter
    parser_classes = [parsers.MultiPartParser]
    
    @docs.LISTPRODUCT
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @docs.CREATEPRODUCT
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @docs.GETPRODUCT
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @docs.UPDATEPRODUCT
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @docs.swagger_auto_schema(auto_schema=None)
    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed("DELETE method is not allowed on this endpoint") 
    
    @docs.swagger_auto_schema(auto_schema=None)
    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed("PATCH method is not allowed on this endpoint")
    
    

class ProductImageViewSet(CreateModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    # permission_classes = [IsAuthenticated]
    parser_classes = [parsers.MultiPartParser]
    
    @docs.CREATEPRODUCTIMAGE
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @docs.UPDATEPRODUCTIMAGE
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @docs.swagger_auto_schema(auto_schema=None)
    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed("PATCH method is not allowed on this endpoint")
    
    @docs.DELETEPRODUCTIMAGE
    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_204_NO_CONTENT)
    
    
    
    
    
    
    