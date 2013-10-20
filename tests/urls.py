# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include

urlpatterns = patterns('', (r'^', include('blackhole.urls')))
