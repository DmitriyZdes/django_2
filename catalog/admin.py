from django.contrib import admin
from catalog.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'price', 'category')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name',)
