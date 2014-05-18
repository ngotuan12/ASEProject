'''
Created on Apr 3, 2014

@author: TuanNA
'''
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.shortcuts import render, render_to_response
from mongoengine.django.auth import User

from myapp.models import Comment
from myapp.models.CommentPost import CommentPost
from myapp.models.Curriculumn import Curriculumn
from myapp.models.Material import Material
from myapp.models.MentorPost import MentorPost
from myapp.util import context_processors
from myapp.models.CurriculumnStudyProgress import CurriculumnStudyProgress


@login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':
		vCourse_id = request.GET['course_id']
		cl = Curriculumn.objects.get(id=vCourse_id)
		progress = CurriculumnStudyProgress.objects(curriculumn=cl,user=request.user)
		is_joined = False
		if len(progress)>0:
			is_joined = True
		#comments = CommentPost.objects(post_id=vpost_id).all()
		#comments = cl.comments
		context = {	'cl':cl,'is_joined':is_joined,
					'user_id':request.user,
					'course_id':vCourse_id
					}
		return render(request, 'myapp/course-detail.html', context)
	elif request.method == 'POST':
		comment = request.POST['txtComment']
		course_id = request.POST['hd_course_id']
		material_id = request.POST['hd_material_id']
		user_id = request.session['_auth_user_id']
		ur = request.user
		cmt = Comment()
		cmt.user = request.user
		cmt.content=comment
		cmt.save()# 		user_id = request.session
		cl = Curriculumn.objects.get(id=course_id)
		mt = Material.objects.get(id=material_id)
		mt.comment.append(cmt);
		mt.save()
		cl.save()
# 		comments = CommentPost.objects(post_id=post_id).all()
		cl = Curriculumn.objects.get(id=course_id)
		context = {	'cl':cl,
					'user_id':request.user,
					'course_id':course_id
					}
		context.update(csrf(request))
		context.update(context_processors.user(request))
		return render_to_response("myapp/course-detail.html", context)