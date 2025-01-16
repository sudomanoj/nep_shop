from django.urls import path, include
from .views import (
    CategoryViewSet,
    ProductViewSet,
    ProductImageViewSet,
    )
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'category', CategoryViewSet, basename='category')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'product-image', ProductImageViewSet, basename='product-image')

urlpatterns = [
    path('', include(router.urls)),
]