'''
Created on Apr 3, 2014

@author: TuanNA
'''
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from myapp.models import MentorPost ,UserProfile
from mongoengine.django.auth import User

from django.http import HttpResponseRedirect

@login_required(login_url='/signin')
def index(request):
	try:
		user_id=request.session['_auth_user_id']
		print(user_id)
		use=User.objects.get(id=user_id).id
		print(use)
		profiles = UserProfile.objects(user_id=User.objects.get(id=user_id)).first()
		if(profiles==None):
			_profile = UserProfile()
			_profile.user_id = request.user
			_profile.save()
			return HttpResponseRedirect('/create-profile')
		
	except Exception as e:
		print(e)
	
	posts = MentorPost.objects
	user_type = ""
	try:
		user_type = request.session['user_type']
	except Exception:
		user_type = ""
	context = {'posts':posts,'user_type':user_type,'user_id':request.user,}
	return render(request,'myapp/index.html', context)