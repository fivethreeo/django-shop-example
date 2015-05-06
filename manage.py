#!/usr/bin/env python

import os
from django.utils._os import upath

import app_manage

MEDIA_ROOT=os.path.join(os.path.dirname(upath(__file__)), "media")

if __name__ == '__main__':
    app_manage.main(
        [
            'shop_example',
            'shop',
            'shop_categories',
            'mptt',
            'treeadmin',
            'tinymce',
            'better_test', 
            'django.contrib.contenttypes',
            'django.contrib.auth',
            'django.contrib.sessions',
            'django.contrib.admin',
            'django.contrib.sites',
            'django.contrib.staticfiles'
        ],
        DEBUG=True,
        SITE_ID=1,
        DATABASES=app_manage.DatabaseConfig(
            default='sqlite:///shopexampledb.sqlite'
        ),
        ROOT_URLCONF='shop_example.urls',
        SHOP_PRODUCT_MODEL = 'shop_example.models.product.Product',
        SHOP_ADDRESS_MODEL = 'shop_example.models.address.Address',
        SHOP_CATEGORIES_CATEGORY_MODEL = 'shop_example.models.category.Category',
        SHOP_PAYMENT_BACKENDS = [
            'shop.payment.backends.pay_on_delivery.PayOnDeliveryBackend'
        ],
        SHOP_SHIPPING_BACKENDS = [
            'shop.shipping.backends.flat_rate.FlatRateShipping'
        ],
        STATIC_ROOT=app_manage.TempDir(),
        MEDIA_ROOT=os.path.join(os.path.dirname(upath(__file__)), "media")
    )
