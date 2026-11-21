from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


class UserProfile(AbstractUser):
    delivery_address = models.CharField(max_length=255)
    phone_number = PhoneNumberField(default='+996')
    avatar = models.ImageField(upload_to='profile_images/')
    date_register = models.DateTimeField(auto_now_add=True)

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logo/', blank=True, null=True)
    address = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    delivery_time = models.CharField(max_length=50, default='30-45 мин')
    min_order_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_open = models.BooleanField(default=False)

    def get_avg_rating(self):
        ratings = self.product_reviews.all()
        if ratings.exists():
            return round(sum([i.stars for i in ratings]) / len(ratings), 1)
        return 0

class MenuCategory(models.Model):
    name = models.CharField(max_length=50)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='menu_items/', null=True, blank=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)

class Cart(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def get_total_price(self):
        return sum([i.get_total_price() for i in self.item.all()])

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.item.price * self.quantity

class Order(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem, blank=True)
    delivery_address = models.CharField(max_length=255)
    status = models.CharField(
        max_length=50,
        choices=[
            ('pending', 'Ожидает'),
            ('processing', 'Обрабатывается'),
            ('completed', 'Завершён'),
            ('cancelled', 'Отменён'),
        ],
        default='pending'
    )
    created_date = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class RestaurantReview(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)




