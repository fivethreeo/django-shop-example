from django.db import models
from tinymce import models as tinymce_models
from shop_categories.models.defaults.category.base import ProductCategoryBase
        
class Category(ProductCategoryBase):

    image = models.ImageField(upload_to='categorys/', null=True, blank=True)

    class Meta:
        abstract = False
        app_label = 'shop_example'