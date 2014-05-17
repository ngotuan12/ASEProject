'''
Created on Apr 3, 2014
@author: TuanNA
'''
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from myapp.models import Material, MaterialType, UserProfile
from myapp.models.Action import Action
from myapp.models.Curriculumn import Curriculumn
from myapp.models.Mentor import Mentor
from mongoengine.django.auth import User
from bson.objectid import ObjectId


@login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':
		user_id = request.GET['user_id']
		user = User.objects.get(id=user_id)
		user= User()
		obj =  ObjectId("")
		
		
		context = {'mentor':user}
		return render(request,'myapp/mentor-course.html', context)
	elif request.method == 'POST':
		#curriculum
		course_name = request.POST['course_name']
		duration = request.POST['duration']
		duration_type = request.POST['duration_type']
		start_date = request.POST['start_date']
		end_date = request.POST['end_date']
		curriculumn = Curriculumn()
		curriculumn.name = course_name
		curriculumn.duration = duration
		curriculumn.duration_type = duration_type
		curriculumn.from_date = datetime.strptime(start_date,'%m/%d/%Y')
		curriculumn.to_date = datetime.strptime(end_date,'%m/%d/%Y')
		curriculumn.mentor = mentor
		curriculumn.save()
		#material
		material_title = request.POST['material_title']
		material_type = request.POST['material_type']
		material_url = request.POST['material_url']
		material_code = request.POST['material_code']
		material_description = request.POST['material_description']
		material = Material()
		material.name = material_title
		material.type = MaterialType.objects.get(name=material_type)
		material.url = material_url
		material.code = material_code
		material.description = material_description
		material.save()
		curriculumn.material.append(material)
		curriculumn.save()
		#action
		action_name = request.POST['action_name']
		action_description = request.POST['action_description']
		action = Action()
		action.name = action_name
		action.description = action_description
		action.save()
		curriculumn.action.append(action)
		curriculumn.save()
		return HttpResponseRedirect('mentor-course');
		