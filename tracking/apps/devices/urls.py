from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('tracking.apps.devices.views',
	url(r'^devices.add/$','register_device',name='add_device_view'),
	url(r'^devices/$','view_device',name='device_view'),
	# url(r'^login/$','login_view',name='login_view'),
	# url(r'^logout/$','logout_view',name='logout_view'),
)
