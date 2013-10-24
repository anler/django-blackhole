# -*- coding: utf-8 -*-
try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('blackhole.views',
    url(r'^templates/(?P<name>[\w\.\/]+)/raw/$', 'view_raw_template', name='view-raw-template'),
    url(r'^templates/(?P<name>[\w\.\/]+)/$', 'view_template', name='view-template'),
)
