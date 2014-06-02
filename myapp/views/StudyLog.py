'''
Created on Apr 3, 2014
@author: TuanNA
'''
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from mongoengine.django.auth import User

from myapp.models.Curriculumn import Curriculumn
from myapp.models.Mentor import Mentor
from myapp.util import context_processors


@login_required(login_url='/signin')
def index(request):
	mycurriculumn = Curriculumn.objects()
	
	context = {}
	return render(request,'myapp/studyLog.html', context)