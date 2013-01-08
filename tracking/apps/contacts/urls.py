from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('tracking.apps.contacts.views',
	url(r'^contact.add/$','register_contact',name='add_contact_view'),
	url(r'^contacts/$','view_contacts',name='contacts_view'),
	# url(r'^devices/$','view_device',name='device_view'),
)
