#encoding:utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMultiAlternatives 
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Modulos
from django.contrib.auth.models import User
from tracking.apps.contacts.models import contact
# Formularios
from tracking.apps.contacts.forms import frmContact



def register_contact(request):
	if request.method == "POST":
		frm = frmContact(request.POST)
		if frm.is_valid():
			_frm = frm.save(commit=False)
			_frm.user = request.user
			_frm.save()
			return HttpResponseRedirect('/devices/')
		ctx = {'form':frm}
	else:
		ctx = {'form':frmContact}
	return render_to_response('forms/contacts/register.html',ctx,context_instance=RequestContext(request))


def view_contacts(request):
	objContacts = contact.objects.filter(user=request.user)
	ctx = {'contact':objContacts}
	return render_to_response('contacts/all.html',ctx,context_instance=RequestContext(request))

