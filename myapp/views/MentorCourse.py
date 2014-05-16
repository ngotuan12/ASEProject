'''
Created on Apr 3, 2014
@author: TuanNA
'''
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from mongoengine.django.auth import User

from myapp.models.CommentPost import CommentPost
from myapp.models.Esay import Esay
from myapp.models.MentorPost import MentorPost
from myapp.util import context_processors


@login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':
		context = {}
		return render(request,'myapp/mentor-course.html', context)
	elif request.method == 'POST':
		#curriculum
		course_name = request.POST['course_name']
		duration = request.POST['duration']
		duration_type = request.POST['duration_type']
		start_date = request.POST['start_date']
		end_date = request.POST['end_date']
		#material
		material_title = request.POST['material_title']
		material_type = request.POST['material_type']
		material_url = request.POST['material_url']
		material_description = request.POST['material_description']
		#action
		action_name = request.POST['action_name']
		action_description = request.POST['action_description']
		#
		context = {}
		return HttpResponseRedirect('mentor-course');
	