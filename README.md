thefoxbox.com
=============

The Fox Box Website

Requirements
------------

* mod\_wsgi       >= 3.2.x
* Python WebOb    >= 1.2.x
* Python Routes   >= 1.10.x
* Python Pystache >= 0.5.x
* Python Markdown >= 2.3.x
* Python Pygments >= 1.1.x

Apache Configuration
--------------------

    DocumentRoot /opt/www/thefoxbox.com/public_html

    WSGIScriptAlias / /opt/www/thefoxbox.com/wsgi-scripts/app.wsgi

    <Directory /opt/www/thefoxbox.com/public_html/wsgi-scripts>
        AllowOverride None
        Order deny,allow
        Allow from all
    </Directory>

    Alias /site.xml           /opt/www/thefoxbox.com/public_html/site.xml
    Alias /robots.txt         /opt/www/thefoxbox.com/public_html/robots.txt
    Alias /favicon.ico        /opt/www/thefoxbox.com/public_html/favicon.ico
    AliasMatch ^/static/(.*)$ /opt/www/thefoxbox.com/public_html/static/$1
