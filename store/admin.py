from django.contrib import admin
from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    list_filter = ('parent',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    filter_horizontal = ('categories',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

