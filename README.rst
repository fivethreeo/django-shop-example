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
    virtualenv env
    source ./env/bin/activate
    pip install -r requirements.txt
    pip install PIL
    python develop.py manage syncdb --noinput
    python develop.py server

Windows
=======
    
First make sure PIL is available. Then:

::

    git clone https://github.com/fivethreeo/django-shop-example.git
    cd django-shop-example
    virtualenv env --system-site-pakages
    env\Scripts\activate.bat
    python develop.py manage syncdb --noinput
    python develop.py server
        
Point your browser to http://127.0.0.1:8000/
