from django import forms
from django.forms import ModelChoiceField
from django.core import validators
from django.core.exceptions import ValidationError
from django.forms import ModelForm 
from django.db import models
# models
from tracking.apps.contacts.models import contact
from django.contrib.auth.models import User
from tracking.apps.devices.models import device


class frmContact(forms.ModelForm):
	def __init__(self, _user,*args,**kwargs):
		super (frmContact,self).__init__(*args,**kwargs)
		self.fields['device'].queryset =  device.objects.filter(user=_user)

	class Meta:
		model = contact
		exclude =['user','status',]