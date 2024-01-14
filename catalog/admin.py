from django.contrib import admin
from catalog.models import Product, Category, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'id',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('ver_product', 'ver_name', 'ver_number', 'id',)
    search_fields = ('ver_product',)
    filter = ('is_current_ver',)
