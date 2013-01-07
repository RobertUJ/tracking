#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from tracking.apps.devices.models import device

class alert(models.Model):
	user = models.ForeignKey(User)
	device_alert = models.ForeignKey(device)
	date = models.DateTimeField(auto_now=True)
	latitude = models.CharField(max_length=250)
	longitude = models.CharField(max_length=250)
	point_map = models.CharField(max_length=250)
	alert_sent = models.BooleanField(default=False)
	status = models.BooleanField(default=True)

	def __unicode__(self):
		return "%s -- %s" % (self.user,self.date) 





