#!/usr/bin/env python
from djeasytests.testsetup import TestSetup, default_settings

default_settings.update(dict(
    ROOT_URLCONF='shop_example.urls',
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'shopexampledb.sqlite',
        }
    },
    INSTALLED_APPS = [
        'shop_example',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
        'django.contrib.sites',
        'django.contrib.staticfiles', 
        'shop',
        'shop_categories',
        'mptt',
        'treeadmin',
        'south',
        'tinymce'
    ],
    SHOP_PRODUCT_MODEL = 'shop_example.models.product.Product',
    SHOP_ADDRESS_MODEL = 'shop_example.models.address.Address',
    SHOP_CATEGORIES_CATEGORY_MODEL = 'shop_example.models.category.Category',
    SHOP_PAYMENT_BACKENDS = [
        'shop.payment.backends.pay_on_delivery.PayOnDeliveryBackend'
    ],
    SHOP_SHIPPING_BACKENDS = [
        'shop.shipping.backends.flat_rate.FlatRateShipping'
    ]  
))

testsetup = TestSetup(appname='shop_example', default_settings=default_settings)

if __name__ == '__main__':
    testsetup.run('shell')