from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^funds/', include('isatracker.funds.urls')),
    (r'^isas/', include('isatracker.isas.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/isas/'}),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/home/adam/Code/Python/isatracker/media'}),
)
