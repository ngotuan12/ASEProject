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
	if request.method == 'GET':
		user = User.objects.get(username=str(request.user))
		user_id = user.id
		cuongnm="alo cuongnm"
		
		context = {'user_id':user_id,
					'cuongnm':cuongnm
				}
		return render(request,'myapp/studyLog.html', context)
	elif request.method == 'POST':
		user_id = request.POST['user_id'];
		datacontent = request.POST['datacontent'];
		
		custom_param1 = request.POST['custom_param1'];
		custom_param2 = request.POST['custom_param2'];
		
		
		cuongnm = datacontent
		print(custom_param1)
		print(custom_param2)
		
		context = {'user_id':user_id,
					'cuongnm':cuongnm
				}
		return render(request,'myapp/studyLog.html', context)
