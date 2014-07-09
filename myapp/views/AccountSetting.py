import json

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from mongoengine.django.auth import User

from myapp.models.UserProfile import UserProfile


@login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':
		user=User.objects.get(username=str(request.user))
		thisupro = UserProfile.objects(user_id=user)[:1]
		context={"UserProfile":thisupro[0]}
		return render(request, 'myapp/account-setting.html', context)
	elif request.method == 'POST':
		fromType = request.POST['formType']
		if	fromType == "frmImage" :
			err_message=""
			
			try:
				print("DO thing here when post")
				
				
				success="successful"
			except Exception as e:
				print(e)
				err_message = e
			return HttpResponse(json.dumps({"formdata": err_message,"success": success}),content_type="application/json")
		elif fromType == "frmProfile" :
			err_message=""
			success=""
			try:
				txtJob = request.POST['txtJob']
				txtCompany = request.POST['txtCompany']
				txtWorking = request.POST['txtWorking']
				txtEducation = request.POST['txtEducation']
				txtSkill = request.POST['txtSkill']
				txaAbout = request.POST['txaAbout']
				user=User.objects.get(username=str(request.user))
				thisupro = UserProfile.objects(user_id=user)[:1]
				if len(thisupro)>0:
					supro=thisupro[0]
					supro.job_title = txtJob
					supro.company = txtCompany
					supro.work_field = txtWorking
					supro.edu = txtEducation
					supro.skill = txtSkill
					supro.about = txaAbout
					supro.save()
					success="success"
			except Exception as e:
				print(e)
				err_message = e
				success=e
			return HttpResponseRedirect('/account-setting')