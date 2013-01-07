from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('tracking.apps.users.views',
	url(r'^register.accounts/$','register_user',name='register_view'),
	url(r'^login/$','login_view',name='login_view'),
	url(r'^logout/$','logout_view',name='logout_view'),
)
