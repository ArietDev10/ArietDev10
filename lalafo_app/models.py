from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=64, unique=True)
    category_image = models.ImageField(upload_to='category_images/')

    def __str__(self):
        return self.category_name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    product_image = models.ImageField(upload_to='product_images/')
    description = models.TextField(null=True, blank=True)
    product_type = models.BooleanField(default=False)
    address = models.CharField(max_length=150, null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.category.category_name} - {self.product_name}'