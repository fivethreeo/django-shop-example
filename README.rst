===================
django-shop-example
===================

A django shop example

How to run
----------

Linux
======

::

    git clone https://github.com/fivethreeo/django-shop-example.git
    cd django-shop-example
    virtualenv shop_env
    source ./shop_env/bin/activate
    pip install -r requirements.txt
    pip install PIL
    python runtestserver.py

Windows
=======
    
First make sure PIL is available. Then:

::

    git clone https://github.com/fivethreeo/django-shop-example.git
    cd django-shop-example
    virtualenv shop_env --system-site-pakages
    shop_env\Scripts\activate.bat
    pip install -r requirements.txt
    python runtestserver.py
        
Point your browser to http://127.0.0.1:8080/
