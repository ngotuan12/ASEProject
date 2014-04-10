'''
Created on Apr 3, 2014

@author: TuanNA
'''
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from mongoengine.django.auth import User

from myapp.models.JobTitle import JobTitle
from myapp.models.UserProfile import UserProfile
from myapp.models.WorkField import WorkFeild
from myapp.util import context_processors


@login_required(login_url='/signin')
def index(request):
	try:
		profiles = UserProfile.objects
		context = {'profiles':profiles,}
		return render(request, 'myapp/chat.html', context)
	except Exception:
		profile = UserProfile()
		profile.user_id = User.objects.get(id=user_id)
		context = {'profile':profile,}
		return render(request, 'myapp/chat.html', context)