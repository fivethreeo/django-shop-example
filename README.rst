===================
django-shop-example
===================

A django shop example

How to run
----------

::

    git clone https://github.com/fivethreeo/django-shop-example.git
    cd django-shop-example
    virtualenv shop_env  # --system-site-pakages for PIL on windows
    source ./shop_env/bin/activate
    pip install -r requirements.txt
    pip install PIL # if you did not use --system-site-pakages on Linux
    python runtestserver.py
    
Point your browser to http://127.0.0.1:8080/
