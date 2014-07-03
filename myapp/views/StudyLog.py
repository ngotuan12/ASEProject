'''
Created on Apr 3, 2014
@author: TuanNA
'''

import json

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render, render_to_response
from mongoengine.django.auth import User

from myapp.models.Curriculumn import Curriculumn
from myapp.models.Mentor import Mentor
from myapp.models.StudyLog import StudyLog
from myapp.util import context_processors


@login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':
		username=request.user
		print(request.user)
		lisCurriculumns = Curriculumn.objects()
		
		user=User.objects.get(username=str(request.user))
		studylog = StudyLog.objects(user=user)[:1]
		datalog=""
		flag = 1 ;
		if len(studylog) == 0:
			flag = 0
		else:
			datalog=studylog[0].data
			
		context = {'username':username,
					'lisCurriculumns':lisCurriculumns,
					'datalog': datalog,
					'flag' : flag
				}
		return render(request,'myapp/studyLog.html', context)
	
	elif request.method == 'POST':
		err_message=""
		try:
			datacontent = request.POST['datacontent']
			user=User.objects.get(username=str(request.user))
			studylog = StudyLog.objects(user=user)[:1]
			
			if len(datacontent) >0:
				print(datacontent)
				
				if len(studylog) >0:
					print('update')
					st=studylog[0]
					st.data=str(datacontent)
					st.save()
				else:
					print('insert')
					study = StudyLog()
					study.user = user
					study.data = datacontent
					study.save()
		except Exception as e:
			print(e)
			err_message = e
		return HttpResponse(json.dumps({"formdata": err_message }),content_type="application/json")