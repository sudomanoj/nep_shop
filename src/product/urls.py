from django.urls import path, include
from .views import (
    CategoryViewSet,
    ProductViewSet,
    ProductImageViewSet,
    RatingViewSet
    )
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'category', CategoryViewSet, basename='category')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'product-image', ProductImageViewSet, basename='product-image')
router.register(r'rating', RatingViewSet, basename='rating')

urlpatterns = [
    path('', include(router.urls)),
]