from modeltranslation.translator import TranslationOptions,register
from .models import *

@register(MenuCategory)
class CategoryTranslationOptions(TranslationOptions):
    filter = ('name',)

@register(Restaurant)
class SubCategoryTranslationOptions(TranslationOptions):
    filter = ('name',)

@register(MenuItem)
class ProductTranslationOptions(TranslationOptions):
    filter = ('name', 'description',)

@register(Cart)
class ProductTranslationOptions(TranslationOptions):
    filter = ('user',)

@register(CartItem)
class ProductTranslationOptions(TranslationOptions):
    filter = ('cart',)

@register(Order)
class ProductTranslationOptions(TranslationOptions):
    filter = ('user',)

@register(MenuItem)
class ProductTranslationOptions(TranslationOptions):
    filter = ('name', 'description',)

@register(OrderItem)
class ProductTranslationOptions(TranslationOptions):
    filter = ('order',)

@register(RestaurantReview)
class ProductTranslationOptions(TranslationOptions):
    filter = ('restaurant',)