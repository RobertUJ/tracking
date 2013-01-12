from django import forms
from django.forms import ModelChoiceField
from django.core import validators
from django.core.exceptions import ValidationError
from django.forms import ModelForm 
from django.db import models
# models
from tracking.apps.contacts.models import contact
from django.contrib.auth.models import User


class frmContact(forms.ModelForm):
	class Meta:
		model = contact
		exclude =['user','status','device']