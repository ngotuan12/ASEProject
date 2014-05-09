'''
Created on Apr 3, 2014

@author: TuanNA
'''
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.shortcuts import render, render_to_response
from mongoengine.django.auth import User

from myapp.models.CommentPost import CommentPost
from myapp.models.MentorPost import MentorPost
from myapp.util import context_processors

# @login_required(login_url='/signin')
def index(request):
	if request.user is None:
		return render(request, 'myapp/home.html', {})
	elif request.method == 'GET':
		posts = MentorPost.objects
		user_type = ""
		try:
			user_type = request.session['user_type']
		except Exception:
			user_type = ""
			
		context = {'posts':posts,'user_type':user_type,'user_id':request.user,}
		return render(request,'myapp/index.html', context)
#		return render(request, 'myapp/home.html', {})
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
		post.comments.append(cmt);
		post.save()
		user_type = ""
		try:
			user_type = request.session['user_type']
		except Exception:
			user_type = ""
		context = {'post':post,'user_type':user_type,'user_id':request.user,}
		context.update(csrf(request))
		context.update(context_processors.user(request))
		return render_to_response("myapp/index.html", context)