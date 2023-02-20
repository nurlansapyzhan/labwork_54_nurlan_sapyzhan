from django.contrib import admin

from labwork54.models import Product, Category


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'description', 'category', 'added_date', 'price', 'image')
    list_filter = ('product_name', 'category', 'added_date', 'price')
    search_fields = ('product_name', 'category', 'price')
    fields = ('product_name', 'description', 'category', 'added_date', 'price', 'image')
    readonly_fields = ('id', 'added_date')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_description')
    list_filter = ('category_name', 'category_description')
    fields = ('category_name', 'category_description')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
