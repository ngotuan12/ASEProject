#from django.shortcuts import render

from django.contrib.auth import login,logout
from django.core.context_processors import csrf
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from mongoengine.django.auth import User
import mongoengine
from myapp.models import UserLogin


# ...
#from myapp.models import BlogPost
def index(request):
	
	#blog = BlogPost(title="abc")
	#blog.published_date = datetime(2014,1,6,0,0,0)
	#blog.save()
	#for blog in BlogPost.objects:
		#print(blog.title)
	#return HttpResponse(BlogPost.objects);
	
	context = {}
	return render(request, 'myapp/index.html', context)
def profile(request):
	context = {}
	return render(request, 'myapp/profile.html', context)
def people(request):
	context = {}
	return render(request, 'myapp/people-directory.html', context)
def blogSingle(request):
	context = {}
	return render(request, 'myapp/blog-single.html', context)
def signin(request):
	username = ""
	password = ""
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
				return HttpResponseRedirect('/home')
			else:
				c = {
						'error_message':"User name or password does not correct",
						'username':username,
						'password':password,
					}
				c.update(csrf(request))
				return render_to_response("myapp/signin.html", c)
		except Exception as e:
				c = {
						'error_message':e,
					}
				c.update(csrf(request))
				return render_to_response("myapp/signin.html", c)
	return render(request, 'myapp/signin.html', {})
def signup(request):
	firstname = "";
	lastname = "";
	username = "";
	password = "";
	passwordConfirm = "";
	email = "";
	if request.method == 'GET':
		return render(request, 'myapp/signup.html', {})
	elif request.method == 'POST':
		try:
			#parameter
			firstname = request.POST['txtFirstName']
			lastname = request.POST['txtLastName']
			username = request.POST['txtUserName']
			password = request.POST['txtPassWord']
			passwordConfirm = request.POST['txtPassWordConfirm']
			email= request.POST['txtEmail']
			if str(firstname).strip() == "":
				return getSignupError(request,'First name can not be empty!',firstname,lastname,username,password,passwordConfirm,email)
			elif str(lastname).strip() == "":
				return getSignupError(request,'Last name can not be empty!',firstname,lastname,username,password,passwordConfirm,email)
			elif str(username).strip() == "":
				return getSignupError(request,'User name can not be empty!',firstname,lastname,username,password,passwordConfirm,email)
			elif str(password).strip() == "":
				return getSignupError(request,'Pass word can not be empty!',firstname,lastname,username,password,passwordConfirm,email)
			elif password != passwordConfirm:
				return getSignupError(request,'Pass word does not match!',firstname,lastname,username,password,passwordConfirm,email)
			elif str(email).strip() == "":
				return getSignupError(request,'Email can not be empty!',firstname,lastname,username,password,passwordConfirm,email)
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
			return HttpResponseRedirect('/home')
		except mongoengine.errors.ValidationError as ex:
			return getSignupError(request,str(ex.errors['email']),firstname,lastname,username,password,passwordConfirm,email)
		except mongoengine.errors.NotUniqueError as e:
			return getSignupError(request,'User has already exists!',firstname,lastname,username,password,passwordConfirm,email)
		except Exception as e:
			return getSignupError(request,str(e),firstname,lastname,username,password,passwordConfirm,email)
def getSignupError(request,e,firstname,lastname,username,password,passwordConfirm,email):
	c = {
			'error_message':e,
			'firstname':firstname,
			'lastname':lastname,
			'username':username,
			'password':password,
			'passwordConfirm':passwordConfirm,
			'email':email,
		}
	c.update(csrf(request))
	return render_to_response("myapp/signup.html", c)
