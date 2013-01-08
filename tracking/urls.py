from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    # Our url's apps
    url(r'^',include('tracking.apps.main.urls')),
    url(r'^',include('tracking.apps.users.urls')),
    url(r'^',include('tracking.apps.devices.urls')),
    url(r'^',include('tracking.apps.contacts.urls')),
)
