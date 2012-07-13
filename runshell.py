#!/usr/bin/env python
from shop_example.test_utils.cli import configure
from djeasytests.tmpdir import temp_dir

def main():
    with temp_dir(prefix='shop-example') as STATIC_ROOT:
        with temp_dir(prefix='shop-example') as MEDIA_ROOT:
            configure(
                ROOT_URLCONF='shop_example.urls',
                STATIC_ROOT=STATIC_ROOT,
                MEDIA_ROOT=MEDIA_ROOT,
                DATABASES = {
                    'default': {
                        'ENGINE': 'django.db.backends.sqlite3',
                        'NAME': 'shopexampledb.sqlite',
                    }
                }
            )
            from django.core.management import call_command
            call_command('shell')

if __name__ == '__main__':
    main()