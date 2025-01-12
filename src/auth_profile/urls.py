from django.urls import path, include
from .views import (
    UserViewSet,
    StoreViewSet,
    SellerViewSet,
    )
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'store', StoreViewSet, basename='store')
router.register(r'seller', SellerViewSet, basename='seller')

urlpatterns = [
    path('', include(router.urls)),
]