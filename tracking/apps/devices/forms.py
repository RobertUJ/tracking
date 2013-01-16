from django import forms
from django.forms import ModelChoiceField
from django.core import validators
from django.core.exceptions import ValidationError
from django.forms import ModelForm 
from django.db import models
# models
from tracking.apps.devices.models import device
from django.contrib.auth.models import User


class frmDevice(forms.ModelForm):
	class Meta:
		model = device
		exclude =['user','status']