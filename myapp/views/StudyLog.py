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
from myapp.models.Material import Material
from myapp.models.Action import Action
from myapp.models.Mentor import Mentor
from myapp.models.ProgressType import ProgressType
from myapp.models.StudyLog import StudyLog
from myapp.util import context_processors


@login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':
		username=request.user
		user=User.objects.get(username=str(request.user))
		
		listProgress = ProgressType.objects()
		
		listcurrilog = CurriculumnLog.objects(user_id=user).order_by('process','published_date','-curriculumn')
		
		if len(listcurrilog)>0:
			currilog=listcurrilog[0]
		datalog="[]"
		flag = '0' ;
		if len(listcurrilog) > 0:
			flag = '1'
		if len(listcurrilog)>0:
			context = {'username':username,
						'listProgress' : listProgress,
						'listcurrilog': listcurrilog,
						'datalog': datalog,
						'firstcurrilog':currilog,
						'flag' : flag
					}
		else:
			context = {'username':username,
						'listProgress' : listProgress,
						'listcurrilog': listcurrilog,
						'datalog': datalog,
						'flag' : flag
					}
		return render(request,'myapp/studyLog.html', context)
	
	elif request.method == 'POST':
		fromType = request.POST['formType']
		if	fromType == "frmCalendar" :
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
		elif fromType == "frmProgress" :
			err_message=""
			
			try:
				
				currilogid = request.POST['curriculumnlog_id']
				progressid = request.POST['progress_id']
				
				currilog = CurriculumnLog.objects(id=currilogid)[:1]
				newprogress = ProgressType.objects(id=progressid)[:1]
				print(currilogid)
				print(progressid)
				cl = currilog[0]
				cl.process = newprogress[0]
				cl.save()
				success="successful"
			except Exception as e:
				print(e)
				err_message = e
			return HttpResponse(json.dumps({"formdata": err_message,"success": success}),content_type="application/json")