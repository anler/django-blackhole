Django-Blackhole
================

Django application that let's you work in your templates apart from having or not the corresponding views created. This is very useful if you (or a member of your project) are working in a template and don't want to get bothered by if the view of your template is not done or is in an incomplete state or you have to be logged in and so on.
With this plugin you can easily access the template you want to work on, set context data directly via the url or set context data via fixtures.

Features
--------

- Design your template without having the corresponding view created.
- Pass data to your template via the url.
- Specify a json fixture file in the url with your context data.
- Patch Django's url reverse to avoid those annoying url reverse errors when working solely in a template.

Tutorial
--------

In order to start using this plugin, you need to:

1. Add application to your INSTALLED_APPS:
.. code-block:: python

   INSTALLED_APPS += ('blackhole',)

2. Include plugin urls in your project urls:

.. code-block:: python

   if settings.DEBUG:
       urlpatterns += patterns('', ('^_blackhole/', include('blackhole.urls'))

With that in place you should be able to access the url:

``/_blackhole/templates/<template name>/?<template data>``

Let's say you have the following template:

.. code-block:: bash

   myapp/
     templates/
        404.html
        myapp/
          hello.jinja


Accessing the template through an url
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can access those templates through the urls:

``/_blackhole/templates/404.html``

and

``/_blackhole/templates/myapp/hello.jinja``

Passing data to the templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have a **message** variable in **hello.jinja** you can set that variable with:

``/_blackhole/templates/myapp/hello.jinja?message=hola``

You can also set nested values. Let's say you have the variable **person.name** in **hello.jinja**, you can set that variable with:

``/_blackhole/templates/myapp/hello.jinja?person.name=john``

Passing data to the templates via fixtures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your template is too complex to set all the data it needs via the url you can use instead a fixture and specify that fixture via the url. Let's say you have:

.. code-block:: bash

   myapp/
     fixtures/
       myapp_template_data.json
     templates/

If now you access:

``/_blackhole/templates/myapp/hello.jinja?_fixture=myapp_template_data``

The template context will be updated with the context defined in the fixture. For example, if you have the fixture:

.. code-block:: json

  {
    "name": "some name",
    "owner": {
      ...
    }
  }

the template context will have the variable ``name`` set to ``some name`` and the variable ``owner`` set
to the dictionary associated to the owner key in the fixture.


Visualizing the template in raw format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you append ``/raw/`` to the url you can see the template in raw format:

``/_blackhole/templates/myapp/hello.jinja/raw/``

The raw format is just the same response returned with ``text/plain`` as the *Content-Type*.

If you want to receive the response in another Content-Type just set the ``_mime`` param. By default the charset is utf-8 but you can also set it via the ``_charset`` param:

``/_blackhole/templates/myapp/hello.jinja?message=hola&_mime=text/csv&_charset=utf-16``

Installation
------------

To install, simply:

.. code-block:: bash

    $ pip install django-blackhole

Or, directly from the main repository:

.. code-block:: bash

    $ pip install -e git+https://github.com/ikame/django-blackhole.git#egg=blackhole

See `project's website`_ for more information.

.. _project's website: https://github.com/ikame/django-blackhole
