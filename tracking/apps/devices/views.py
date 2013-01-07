#encoding:utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMultiAlternatives 
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Modulos
from django.contrib.auth.models import User
from tracking.apps.users.models import UserProfile
from tracking.apps.devices.models import device
# Formularios
from tracking.apps.devices.forms import frmDevice


@login_required
def register_device(request):
	if request.method == "POST":
		frm = frmDevice(request.POST)
		if frm.is_valid():
			_frm = frm.save(commit=False)
			_frm.user = request.user
			_frm.save()
			return HttpResponseRedirect('/devices/')
		ctx = {'form':frm}
	else:
		ctx = {'form':frmDevice}
	return render_to_response('forms/devices/register.html',ctx,context_instance=RequestContext(request))


@login_required
def view_device(request):
	objDevices = device.objects.filter(user=request.user)
	ctx={'devices':objDevices}
	return render_to_response('devices/all.html',ctx,context_instance=RequestContext(request))
