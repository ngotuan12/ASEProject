#!/usr/bin/env python
# -*- coding: utf8 -*-
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
from myapp.models.CurriculumnLog import CurriculumnLog
from myapp.models.Mentor import Mentor
from myapp.models.ProgressType import ProgressType
from myapp.models.StudyLog import StudyLog
from myapp.util import context_processors


@login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':
		username=request.user
		user=User.objects.get(username=str(request.user))
		print(request.user)
		lisCurriculumns = Curriculumn.objects()
		listABC=[]
		for curriculumn in lisCurriculumns:
			if username in curriculumn.joined_user:
				listABC.append(curriculumn)
		
		listProgress = ProgressType.objects()
		
		listcurrilog = CurriculumnLog.objects(user_id=user)
		
		if len(listcurrilog)>0:
			currilog=listcurrilog[0]
		
		studylog = StudyLog.objects(user=user)[:1]
		datalog="[]"
		flag = 1 ;
		if len(studylog) == 0:
			flag = 0
		else:
			datalog=studylog[0].data
		if len(listcurrilog)>0:
			context = {'username':username,
						'lisCurriculumns':listABC,
						'listProgress' : listProgress,
						'listcurrilog': listcurrilog,
						'datalog': datalog,
						'firstcurrilog':currilog,
						'flag' : flag
					}
		else:
			context = {'username':username,
						'lisCurriculumns':listABC,
						'listProgress' : listProgress,
						'listcurrilog': listcurrilog,
						'datalog': datalog,
						'flag' : flag
					}
		return render(request,'myapp/studyLog.html', context)
	
	elif request.method == 'POST':
		err_message=""
		try:
			datacontent = request.POST['datacontent']
			currilogid = request.POST['curriculumnlog_id']
			user=User.objects.get(username=str(request.user))
			currilog = CurriculumnLog.objects(id=currilogid)[:1]
			
			
			if len(datacontent) >0:
				print(datacontent)
				print(currilogid)
				
				if len(currilog) >0:
					print('update')
					cl=currilog[0]
					cl.data=str(datacontent)
					cl.save()
		except Exception as e:
			print(e)
			err_message = e
		return HttpResponse(json.dumps({"formdata": err_message,"datacontent":datacontent,"currilogid":currilogid }),content_type="application/json")