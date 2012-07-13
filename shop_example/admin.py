from django.contrib import admin
from shop.models import Product
from shop_categories.models import Category
from shop_categories.admin import ProductCategoryAdmin

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
        
admin.site.register(Category, ProductCategoryAdmin)    
admin.site.register(Product, ProductAdmin)
