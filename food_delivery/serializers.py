from rest_framework import serializers
from .models import (UserProfile, Restaurant, MenuCategory, MenuItem, Cart, CartItem, Order, OrderItem, RestaurantReview)

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('delivery_address', 'phone_number', 'avatar', 'date_register')

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('name', 'logo', 'address', 'description', 'delivery_time', 'min_order_price', 'is_open')

class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ('name', 'restaurant')

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('name', 'price', 'description', 'photo', 'weight', 'is_available', 'category')

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('user',)

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('cart', 'item', 'quantity')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('user', 'items', 'delivery_address', 'status')

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('order', 'item', 'quantity')

class RestaurantReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantReview
        fields = ('restaurant', 'user', 'stars', 'comment', 'created_date')
