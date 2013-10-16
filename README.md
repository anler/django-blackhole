Django-Blackhole
================

Django application that let's you work in your templates apart from having or not the corresponding views created.

Features
--------

* Design your template without having the corresponding view created.
* Pass data to your template via the url.

Example
-------

In your urls.py:

```python
if settings.DEBUG:
    urlpatterns += patterns('', ('^_blackhole/', include('blackhole.urls'))
```

With that in place you should be able to access the url: `/_blackhole/templates/<template name>/?<template data>`

Let's say you have the following template:

```
   myapp/
     templates/
        404.html
        myapp/
          hello.jinja
```

### Accessing the template through an url ###

You can access those templates through an url:

`/_blackhole/templates/404.html`

and

`/_blackhole/templates/myapp/hello.jinja`

### Passing data to the templates ###

#### Simple data ####

If you have a `message` variable in `hello.jinja` you can set that variable with:

`/_blackhole/templates/myapp/hello.jinja?message=hola`

#### Sighly complex data ####

You can also set nested values. Let's say you have the variable `person.name` in `hello.jinja`, you can set that variable with:

`/_blackhole/templates/myapp/hello.jinja?person.name=john`

### Visualizing the template in raw format ###

If you append `/raw/` to the url you can see the template in raw format:

`/_blackhole/templates/myapp/hello.jinja/raw/`

The raw format is just the same response returned as `text/plain` instead of as `text/html`

Installation
------------

To install, simply:

```
$ pip install django-blackhole
```

Or, directly from the main repository:

```
$ pip install -e git+http://github.com/ikame/django-blackhole.git#egg=blackhole
```
