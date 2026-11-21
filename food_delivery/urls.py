from rest_framework import routers
from .views import (UserProfileViewSet, RestaurantViewSet, MenuCategoryViewSet, MenuItemViewSet, CartViewSet, CartItemViewSet, OrderViewSet, OrderItemViewSet, RestaurantReviewViewSet)
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'User', UserProfileViewSet)
router.register(r'Restaurant', RestaurantViewSet)
router.register(r'MenuCategory', MenuCategoryViewSet)
router.register(r'Menuitem', MenuItemViewSet)
router.register(r'Cart', CartViewSet)
router.register(r'CartItem', CartItemViewSet)
router.register(r'Order', OrderViewSet)
router.register(r'OrderItem', OrderItemViewSet)
router.register(r'Restaurant', RestaurantReviewViewSet)

urlpatterns = [
    path('', include(router.urls))
]