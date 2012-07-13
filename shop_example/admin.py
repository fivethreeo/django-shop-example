from django.contrib import admin
from shop.models import Product
from shop_categories.models import Category
from shop_categories.admin import ProductCategoryAdmin

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class CategoryAdmin(ProductCategoryAdmin):
    exclude = ('path', 'name_path')
    prepopulated_fields = {"slug": ("name",)}    

admin.site.register(Category, CategoryAdmin)    
admin.site.register(Product, ProductAdmin)
