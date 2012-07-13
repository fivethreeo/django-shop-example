#!/usr/bin/env python
from djeasytests.runtests import runtests_parse
from shop_example.test_utils.cli import configure
    
if __name__ == '__main__':    
    runtests_parse(configure=configure,
        test_labels_prefix='shop_example',
        default_test_labels=['shop_example'],
        tmp_dir_prefix='django-shop-example',
        ROOT_URLCONF='shop_example.urls')