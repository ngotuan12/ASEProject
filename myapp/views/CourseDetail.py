'''
Created on Apr 3, 2014

@author: TuanNA
'''
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.shortcuts import render, render_to_response
from mongoengine.django.auth import User

from myapp.models.CommentPost import CommentPost
from myapp.models.Curriculumn import Curriculumn
from myapp.models.MentorPost import MentorPost
from myapp.util import context_processors


@login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':
		vCourse_id = request.GET['course_id']
		cl = Curriculumn.objects.get(id=vCourse_id)
# 		comments = CommentPost.objects(post_id=vpost_id).all()
		comments = cl.comments
		context = {	'cl':cl,'comments':comments,
					'user_id':request.user,
					}
		return render(request, 'myapp/course-detail.html', context)
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
# 		comments = CommentPost.objects(post_id=post_id).all()
		comments = post.comments
		c = {'post':post,'comments':comments,'user_type':request.session['user_type']}
		c.update(csrf(request))
		c.update(context_processors.user(request))
		return render_to_response("myapp/blog-single.html", c)