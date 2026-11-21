from django.contrib import admin
from .models import (UserProfile, Restaurant, MenuCategory, MenuItem, Cart, CartItem, Order, OrderItem, RestaurantReview)

admin.site.register(UserProfile)
admin.site.register(Restaurant)
admin.site.register(MenuCategory)
admin.site.register(MenuItem)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(RestaurantReview)
