from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('blackhole.views',
    url(r'^templates/(?P<name>[^\/]+)/$', 'view_template', name='view-template'),
    url(r'^templates/(?P<name>[^\/]+)/raw/$', 'view_raw_template', name='view-raw-template'),
)
