#!/usr/bin/env python

import app_manage

if __name__ == '__main__':
    app_manage.main(
        [
            'better_test',
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
            'tinymce'
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
        MEDIA_ROOT=app_manage.TempDir()
    )