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
from myapp.models.Esay import Esay
from myapp.models.Material import Material
from myapp.models.Mentor import Mentor
from myapp.models.MentorPost import MentorPost
from myapp.util import context_processors


@login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':
		#mentor_id = '5375ce146c02298c9af00e00'
		#mentor = Mentor.objects.get(id=mentor_id)
#		cl = Curriculumn.objects(mentor=mentor)
		user_id=request.GET['user_id']
		user = request.user
		print(user.id)
		cl = Curriculumn.objects
		context = {'user_id':user_id,'cl':cl,}
		return render(request,'myapp/studentview.html', context)
	elif request.method == 'POST':
		context.update(context_processors.user(request))
		return render_to_response("myapp/studentview.html", context)