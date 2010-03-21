from django.conf.urls.defaults import *

urlpatterns = patterns('isatracker.isas.views',
    (r'^$', 'index'),
    (r'^(?P<isa_id>\d+)/$', 'show'),
)

