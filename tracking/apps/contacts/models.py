#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User




class contact(models.Model):
	user 	= models.ForeignKey(User)
	name 	= models.CharField(max_length=100,verbose_name='First Name')
	last_name = models.CharField(max_length=255,verbose_name='Last Name')
	email 	= models.CharField(max_length=150,verbose_name='Email')
	phone_number = models.CharField(max_length=100,verbose_name='Phone Number')
	mobile_phone = models.CharField(max_length=100,verbose_name='Mobile Phone')
	relation = models.CharField(max_length=100,verbose_name='Relation')
	primary  = models.BooleanField(default=False)

	def __unicode__(self):
		return "%s %s" % (self.name,self.last_name)
