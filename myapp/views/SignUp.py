'''
Created on Apr 3, 2014

@author: TuanNA
'''
from django.contrib.auth import logout, login
from django.core.context_processors import csrf
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from mongoengine.django.auth import User
import mongoengine.errors

from myapp.models.UserProfile import UserProfile
from myapp.util import context_processors


def index(request):
	firstname = "";
	lastname = "";
	username = "";
	password = "";
	email = "";
	if request.method == 'GET':
		return render(request, 'myapp/signup.html', {'rangerDay':range(1,32),'rangerYear':range(2014,1905,-1),})
	elif request.method == 'POST':
		try:
			#parameter
			firstname = request.POST['txtFirstName']
			lastname = request.POST['txtLastName']
			username = request.POST['txtUserName']
			password = request.POST['txtPassWord']
			email= request.POST['txtEmail']
			if str(firstname).strip() == "":
				return getSignupError(request,'First name can not be empty!',firstname,lastname,username,password,email)
			elif str(lastname).strip() == "":
				return getSignupError(request,'Last name can not be empty!',firstname,lastname,username,password,email)
			elif str(username).strip() == "":
				return getSignupError(request,'User name can not be empty!',firstname,lastname,username,password,email)
			elif str(password).strip() == "":
				return getSignupError(request,'Pass word can not be empty!',firstname,lastname,username,password,email)
			elif str(email).strip() == "":
				return getSignupError(request,'Email can not be empty!',firstname,lastname,username,email)
			#insert new user
			user = User()
			user.username = username
			user.first_name = firstname
			user.last_name = lastname
			user.email = email
			user.set_password(password);
			user.save()
			user.backend = 'mongoengine.django.auth.MongoEngineBackend'
			logout(request)
			login(request, user)
			#create new profile
			_profile = UserProfile()
			_profile.user_id = request.user
			_profile.is_mentor = False
			_profile.save()
			return HttpResponseRedirect('/home')
		except mongoengine.errors.ValidationError as ex:
			return getSignupError(request,str(ex.errors['email']),firstname,lastname,username,password,email)
		except mongoengine.errors.NotUniqueError as e:
			return getSignupError(request,'User has already exists!',firstname,lastname,username,password,email)
		except Exception as e:
			return getSignupError(request,str(e),firstname,lastname,username,password,email)
def getSignupError(request,e,firstname,lastname,username,password,email):
	c = {
			'error_message':e,
			'firstname':firstname,
			'lastname':lastname,
			'username':username,
			'password':password,
			'email':email,
			'rangerDay':range(1,31),
			'rangerYear':range(2014,1905,-1),
		}
	c.update(csrf(request))
	c.update(context_processors.user(request))
	return render_to_response("myapp/signup.html", c)