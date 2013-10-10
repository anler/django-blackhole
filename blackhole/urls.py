from django.conf.urls.defaults import patterns


urlpatterns = patterns('blackhole.views',
    (r'^templates/(?P<name>[\w\.\/]+)', 'view_template'),
)
