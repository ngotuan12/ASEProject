'''
Created on Apr 3, 2014

@author: TuanNA
'''
from django.contrib.auth import logout, login
from django.core.context_processors import csrf
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from mongoengine.django.auth import User

from myapp.models.Mentor import Mentor
from myapp.models.Student import Student
from myapp.models.UserLogin import UserLogin
from myapp.models.UserProfile import UserProfile
from myapp.util import context_processors



def index(request):
	username = ""
	password = ""
	is_mentor=False
	if request.method == 'GET':
		return render(request, 'myapp/signin.html', {})
	elif request.method == 'POST':
		username = request.POST['txtUserName']
		password = request.POST['txtPassWord']
		try: 
			user = User.objects.get(username=username)
			transaction = UserLogin()
			transaction.user = user
			transaction.save()
			if user.check_password(password):
				logout(request)
				user.backend = 'mongoengine.django.auth.MongoEngineBackend'
				login(request, user)
				profile = UserProfile.objects.get(user_id=user)
				request.session['user_images'] = profile.images
				
				mentor = Mentor.objects(user=user)
				if len(mentor) > 0:
					is_mentor = True
				request.session['is_mentor'] = is_mentor
				
				if is_mentor:
					return HttpResponseRedirect('/mentor-course?user_id='+str(user.id))	
				else:
					return HttpResponseRedirect('/student-home')
					#return HttpResponseRedirect('/search-mentor')
			else:
				c = {
						'error_message':"User name or password does not correct",
						'username':username,
						'password':password,
					}
				c.update(csrf(request))
				c.update(context_processors.user(request))
				return render_to_response("myapp/signin.html", c)
		except Exception as e:
				c = {
						'error_message':e,
					}
				c.update(csrf(request))
				c.update(context_processors.user(request))
				return render_to_response("myapp/signin.html", c)
	return render(request, 'myapp/signin.html', {})