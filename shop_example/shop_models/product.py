from django.db import models
from tinymce import models as tinymce_models
from shop_categories.models.defaults.product.base import CategoryProductBase

class Product(CategoryProductBase):
    
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    body = tinymce_models.HTMLField()

    class Meta:
        abstract = False
        app_label = 'shop_example'