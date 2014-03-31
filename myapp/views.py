#from django.shortcuts import render

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf, request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
import mongoengine
from mongoengine.django.auth import User

from myapp.models import UserLogin, MentorPost, CommentPost, JobTitle, WorkFeild, UserProfile


# ...
#from myapp.models import BlogPost
def index(request):
	#collection.setObjectClass(MentorPost.class);
	#blog = BlogPost(title="abc")
	#blog.published_date = datetime(2014,1,6,0,0,0)
	#blog.save()
	#for blog in BlogPost.objects:
		#print(blog.title)
	#return HttpResponse(BlogPost.objects);
	posts = MentorPost.objects
	for post in posts:
		print(post.imagelink)
		
	context = {'user':request.user,'posts':posts,}
	return render_to_response('myapp/index.html', context)
@login_required(login_url='/signin')
def profile(request):
	profile = UserProfile.objects(user_id=request.user)
	context = {'profile':profile,}
	return render(request, 'myapp/profile.html', context)
def people(request):
	context = {}
	return render(request, 'myapp/people-directory.html', context)
def mentorpost(request):
	if request.method == 'GET':
		print("method is get")
		context={}
		return render(request, 'myapp/mentor-post.html', context)
	elif request.method == 'POST':
		print("method is get")
		Title = request.POST['txtTitle']
		Imagelink = request.POST['txtImagelink']
		Amazonlink = request.POST['txtAmazonlink']
		Content = request.POST['txtContent']
		IsLecture=request.POST['slPostType']
		FromDate = request.POST['dtpfromdate']
		ToDate = request.POST['dtptodate']
		Place= request.POST['txtPlace']
		user_id = User.objects.get(id=request.session['_auth_user_id'])
		print(user_id)
		mp = MentorPost()
		mp.title=Title
		mp.imagelink=Imagelink
		mp.amazonlink=Amazonlink
		mp.content=Content
		mp.user_id=user_id
		mp.is_lecture=IsLecture
		mp.status="1"
		mp.from_date=FromDate
		mp.to_date=ToDate
		mp.place=Place
		mp.save()
		return HttpResponseRedirect('/home')
def blogSingle(request):
	if request.method == 'GET':
		vpost_id = request.GET['post_id']
		post = MentorPost.objects.get(id=vpost_id)
		print(vpost_id)
		
		comments = CommentPost.objects(post_id=vpost_id).all()
		
		context = {'post':post,'comments':comments,}
		return render(request, 'myapp/blog-single.html', context)
	elif request.method == 'POST':
		comment = request.POST['txtComment']
		post_id = request.POST['hd_post_id']
		user_id = request.session['_auth_user_id']
		cmt = CommentPost()
		cmt.content=comment
		cmt.user_id=User.objects.get(id=user_id)
		cmt.post_id=MentorPost.objects.get(id=post_id)
		cmt.save()# 		user_id = request.session
		post = MentorPost.objects.get(id=post_id)
		comments = CommentPost.objects(post_id=post_id).all()
		c = {'post':post,'comments':comments,}
		c.update(csrf(request))
		return render_to_response("myapp/blog-single.html", c)
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
			return HttpResponseRedirect('/create-profile')
		except mongoengine.errors.ValidationError as ex:
			return getSignupError(request,str(ex.errors['email']),firstname,lastname,username,password,email)
		except mongoengine.errors.NotUniqueError as e:
			return getSignupError(request,'User has already exists!',firstname,lastname,username,password,email)
		except Exception as e:
			return getSignupError(request,str(e),firstname,lastname,username,password,email)
def createProfile(request):
	context = {}
	return render(request, 'myapp/create-profile.html', context)
def updateProfile(request):
	if request.method == 'GET':
		job_titles = JobTitle.objects
		work_fields = WorkFeild.objects
		context = {'job_titles':job_titles,'work_fields':work_fields,'acccount_type':request.GET['acccount_type'],}
		return render(request, 'myapp/create-profile-update.html', context)
	elif request.method == 'POST':
		try:
			acccount_type = request.POST['acccount_type']
			print(request.POST['slJobTitle'])
			print(request.POST['slWorkField'])
			print(acccount_type)
			return HttpResponseRedirect('/home')
		except Exception as e:
			print(e)
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
	return render_to_response("myapp/signup.html", c)
def signout(request):
	logout(request)
	return HttpResponseRedirect('/signin')
def accountSetting(request):
	
	context = {'userprofile':user_profile}
	return render(request, 'myapp/account-setting.html', context)
