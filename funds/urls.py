from django.conf.urls.defaults import *

urlpatterns = patterns('isatracker.funds.views',
    (r'^$', 'index'),
    (r'^(?P<fund_id>\d+)/$', 'show'),
    (r'^update_prices/$', 'update_prices'),
)

