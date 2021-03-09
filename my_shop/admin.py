from django.contrib import admin

# Register your models here.
from .models import Product, Category, Size

class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "price", "price_with_sale", "description")

admin.site.register(Product)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name")
    search_fields = ("name")
admin.site.register(Category)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("size", "id")
admin.site.register(Size)
