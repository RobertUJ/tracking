#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User


class device(models.Model):
	user 				= models.ForeignKey(User)
	name 				= models.CharField(verbose_name='Name',help_text='Can be any name, to identify the device', max_length=150)
	serial_number 		= models.CharField(verbose_name='Serial Number', max_length=100)
	model 				= models.CharField(verbose_name='Model', max_length=100)
	status  			= models.BooleanField(verbose_name='Status',default=False)
	installed_workshop  = models.BooleanField(verbose_name="Installed in our workshop",default=False)
	def __unicode__(self):
		return "%s"%self.name
	
