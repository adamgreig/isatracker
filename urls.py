from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^funds/', include('isatracker.funds.urls')),
    (r'^admin/', include(admin.site.urls)),
)
