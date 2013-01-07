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
# Formularios
from tracking.apps.users.forms import frmUserReg,frmUserProf,LoginForm


def login_view(request):
	strMsg =""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			objForm = LoginForm(request.POST)
			if objForm.is_valid():
				username = objForm.cleaned_data['username']
				password = objForm.cleaned_data['password']
				objUser = authenticate(username=username,password=password)
				if objUser is not None and objUser.is_active:
					login(request,objUser)
					return HttpResponseRedirect("/")
				else:
					strMsg = "Username Or Password Incorrect"
		objForm = LoginForm()
		ctx = {'form': objForm,'msg':strMsg}
		return render_to_response('forms/accounts/login.html',ctx,context_instance=RequestContext(request))


def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')




def register_user(request):
	if request.method == "POST":
		frm_user = frmUserReg(request.POST)
		frm_profile = frmUserProf(request.POST)
		if frm_user.is_valid() and frm_profile.is_valid():
			username_ = frm_user.cleaned_data['username']
			email_ = frm_user.cleaned_data['email']
			password_ = frm_user.cleaned_data['password']
			new_user = User.objects.create_user(username= username_, email= email_,password=password_)
			new_user.is_staff = False
			new_user.first_name = frm_user.cleaned_data['first_name']
			new_user.last_name 	= frm_user.cleaned_data['last_name']
			new_user.save()
			
			# Profile User
		
			_profile = UserProfile.objects.get(user=new_user)
			_profile.address = frm_profile.cleaned_data['address']
			_profile.city = frm_profile.cleaned_data['city']
			_profile.state = frm_profile.cleaned_data['state']
			_profile.zip_code = frm_profile.cleaned_data['zip_code']
			_profile.dtl_code = frm_profile.cleaned_data['dtl_code']
			_profile.phone = frm_profile.cleaned_data['phone']
			_profile.mobile = frm_profile.cleaned_data['mobile']
			_profile.date_purchased = frm_profile.cleaned_data['date_purchased']
			_profile.license = frm_profile.cleaned_data['license']
			_profile.read_terms = frm_profile.cleaned_data['read_terms']
			_profile.status_membership = False
			
			_profile.save()


			return HttpResponseRedirect('/')
	else:
		frm_user = frmUserReg()
		frm_profile = frmUserProf()
	ctx = {'form':frm_user,'frmProfile':frm_profile}
	return render_to_response('forms/accounts/register.html',ctx,context_instance=RequestContext(request))

