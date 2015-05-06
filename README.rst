===================
django-shop-example
===================

A django shop example that works on django 1.8

How to run
----------

Linux
======

::

    git clone https://github.com/fivethreeo/django-shop-example.git
    cd django-shop-example
    
    npm init
    npm install grunt --save-dev 
    npm install grunt-contrib-concat --save-dev
    npm install grunt-contrib-less --save-dev
    npm install grunt-contrib-uglify --save-dev
    npm install grunt-contrib-watch --save-dev
    npm install grunt-contrib-copy --save-dev

    npm install -g bower
    
    bower install bootstrap -S

    grunt concat less uglify copy

    virtualenv shop_env
    
    source ./shop_env/bin/activate
    pip install -r requirements.txt
    pip install PIL
    pip uninstall south # fix setup.py issues with 3rdparty for django 1.8
    
    python manage.py syncdb --no-initial-data
    python manage.py syncdb # to load fixtures with natural keys, fails if tables are not present
    python manage.py runserver --insecure

    # testing using django-better-test
    python manage.py help test

Windows
=======
    
First make sure PIL is available. Then:

::

    git clone https://github.com/fivethreeo/django-shop-example.git
    cd django-shop-example
    
    npm init
    npm install grunt --save-dev 
    npm install grunt-contrib-concat --save-dev
    npm install grunt-contrib-less --save-dev
    npm install grunt-contrib-uglify --save-dev
    npm install grunt-contrib-watch --save-dev
    npm install grunt-contrib-copy --save-dev
    npm install -g bower
    
    bower install bootstrap -S

    grunt concat less uglify copy
    
    virtualenv shop_env --system-site-packages
    
    shop_env\Scripts\activate.bat
    pip install -r requirements.txt
    pip uninstall south # fix setup.py issues with 3rdparty for django 1.8
    
    python manage.py syncdb --no-initial-data
    python manage.py syncdb # to load fixtures with natural keys, fails if tables are not present
    python manage.py runserver --insecure
    
    # testing using django-better-test
    python manage.py help test
        
Point your browser to http://127.0.0.1:8000/
