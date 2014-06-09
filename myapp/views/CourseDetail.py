'''
Created on Apr 3, 2014

@author: TuanNA
'''
from datetime import datetime
import json

from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from mongoengine.django.auth import User

from myapp.models import Comment, Student, Impression
from myapp.models.Curriculumn import Curriculumn
from myapp.models.CurriculumnLog import CurriculumnLog
from myapp.models.CurriculumnStudyProgress import CurriculumnStudyProgress
from myapp.models.Material import Material
from myapp.models.ProgressType import ProgressType
from myapp.models.Statistic import Statistic
from myapp.models.StatisticDetail import StatisticDetail
from myapp.util import context_processors


@login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':
		vCourse_id = request.GET['course_id']
		author_id=request.GET['user_id']
		author = User.objects.get(id=author_id)
		cl = Curriculumn.objects(id=vCourse_id)
		has_curriculum = False
		is_mentor = request.session['is_mentor']
		user=User.objects.get(username=str(request.user))
		student=Student.objects.get(user=user.id)

		object_id = "537f051c008ebc68d6419d77"
		print()
		str_user = str(user.id)
		str_user = "53833d5630635f17c4daab02"
		print(str_user)
		#userid = "53833d5630635f17c4daab02"
		status = "1"
		
		mtr = Material.objects()[:1]
		mtid = mtr[0].id
		print(mtid)

		if len(cl):
			has_curriculum = True

		clTaken = 0
		clLike = 0
		mtTaken = 0
		mtLike = 0
		actTaken = 0
		actLike = 0
		mtTotal = 0
		actTotal = 0
		try :
			for c in cl:
				if c.statistic.currentTakenNumber:
					c.statistic.currentTakenNumber=10
					clTaken += c.statistic.currentTakenNumber
				if c.statistic.currentLikeNumber:
					clLike += c.statistic.currentLikeNumber
				
				for mt in c.material:
					if mt.statistic.currentTakenNumber:
						mtTaken += mt.statistic.currentTakenNumber
					if mt.statistic.currentLikeNumber:
						mtLike += mt.statistic.currentLikeNumber
						mtTotal += 1
					mt.__setitem__('name', 'aaaaaaaaa')
					print(mt.name)
				for act in c.action:
					if act.statistic.currentTakenNumber:
						actTaken += act.statistic.currentTakenNumber
					if act.statistic.currentLikeNumber:
						actLike += act.statistic.currentLikeNumber
						actTotal +=1
			print(mtTaken)
			print(mtLike)
			print(actTaken)
			print(actLike)
		except Exception as e:
			print(e)
		progress = CurriculumnStudyProgress.objects(curriculumn=cl[0].id,student=student.id)
		is_joined = False
		if len(progress)>0:
			is_joined = True
		#comments = CommentPost.objects(post_id=vpost_id).all()
		#comments = cl.comments
		#Fix code get like status
		lscl = []
		lscl = cl[0]
		
# 		mtt=Material.objects()[:1]
		st = StatisticDetail()
		st.user = user
		st.object_id = '537f051a008ebc68d6419d75'
		st.status="1"
# 		st.save()
		lscl.__setitem__('name', 'aaaaaasdfsdfdsfsdaaa')
#		print(lscl.__getattribute__('name'))
#		print(lscl.__getattribute__('material'))
		
		for i in lscl.__getattribute__('material'):
			i.note='0'
			print(i.name)
			print(i.id)
			try:
				#is_like = StatisticDetail.objects.get(object_id=str(i.id),status=status,user=user.id)
				is_like = StatisticDetail.objects(object_id=str(i.id),status=status,user=user.id)
				if len(is_like):
					i.note='1'
					i.__getattribute__('statistic').currentLikeNumber -=1
			except Exception as e:
				print(e)
		
		context = {	'cl':lscl,'is_joined':is_joined,
					'user_id':request.user,
					'course_id':vCourse_id,
					'author_id':author_id,
					'author':author.username,
					'is_mentor':is_mentor,
					'clTaken':clTaken,
					'clLike':clLike,
					'mtTaken':mtTaken,
					'mtLike':mtLike,
					'actTaken':actTaken,
					'actLike':actLike,
					'mtTotal':mtTotal,
					'actTotal':actTotal,
					'has_curriculum':has_curriculum,
					}
		return render(request, 'myapp/course-detail.html', context)
	elif request.method == 'POST':
		if request.POST['posttype'] == "likeMaterial":
			user=User.objects.get(username=str(request.user))
			print(request.POST['posttype'])
			materialId=request.POST['materialId']
			status =request.POST['status']#like or dislike
			print(status)
			print('status: '+request.POST['status'])
			print('material: '+request.POST['materialId'])
			print('course: ' +request.POST['courseId'])
			print('author: ' +request.POST['userId'])
			print('user: ' +str(user.id) )
			
			#update status=0 for recors last with status=1,user_id,material
			sdLast=StatisticDetail.objects(user=user.id,object_id=str(materialId),status='1').order_by('published_date')[:10]
			if len(sdLast):
				print('exist, update the last record')
				for sdUpdate in sdLast:
					sdUpdate.status='0'
					sdUpdate.save()
			else:
				print('no update ')
			sdNew=StatisticDetail()
			sdNew.user=user
			sdNew.object_id=str(materialId)
			if status =='0':
				sdNew.status='1'
			else :
				sdNew.status='0'
			sdNew.save()
			#update or insert statistic
			stCurent=Statistic.objects(object_id=str(materialId)).order_by('create_date')[:1]
			stNew=Statistic()
			if len(stCurent) >0:
				print('exist')
				stNew=stCurent[0]
				if status == '1':
					stNew.currentLikeNumber -= 1
				else:
					stNew.currentLikeNumber += 1
				stNew.type='1'
				stNew.save()
			else:
				print('no exist')
				if status == '0':
					stNew.currentLikeNumber=1
				else:
					stNew.currentLikeNumber=0
				stNew.object_id=str(materialId)
				stNew.type='1'
				stNew.save()
			#update material 
			mtCurrent=Material.objects.get(id=materialId)
			mtCurrent.statistic=stNew
			mtCurrent.note='0'
			mtCurrent.save()
			
			return HttpResponse(json.dumps({"formdata": materialId}),content_type="application/json")
		elif request.POST['posttype']== "frmJoincourse":
			curriculum_id = request.POST['curriculum_id']
			user_id=request.POST['user_id']
			print(curriculum_id)
			curriculum = Curriculumn.objects.get(id=curriculum_id)
			
			user=User.objects.get(username=str(request.user))
			student=Student.objects.get(user=user.id)
			
			planstart = request.POST['planstart']
			planend = request.POST['planend']
			impression = request.POST['impression']
			description = request.POST['description']
			# Save CurriculumnStudyProgress
			csp = CurriculumnStudyProgress()
			csp.student=student
			csp.curriculumn = curriculum	
			csp.PlanStartDate = datetime.strptime(planstart,'%m/%d/%Y')
			csp.PlanEndDate = datetime.strptime(planend,'%m/%d/%Y')
			csp.impression = Impression.objects.get(showpiority=impression)
			csp.description = description
			csp.save()
			
			#UPDATE Curriculumn
			print(user.id)
			curri=Curriculumn()
			
			curri = Curriculumn.objects.get(id=curriculum_id)
			curri.joined_user.append(user);
			
			curri.save()
			# Save CurriculumnLog
			lisProgressType = ProgressType.objects()
			progressType =lisProgressType[0]
			
			curriLog=CurriculumnLog()
			
			curriLog.curriculumn=curri
			curriLog.process=progressType
			curriLog.user_id=user
			
			curriLog.save()
			#SHOW Record
			cl = Curriculumn.objects(id=curriculum_id)
			has_curriculum = False
			is_mentor = request.session['is_mentor']
			if len(cl):
				has_curriculum = True
			print(has_curriculum)
			clTaken = 0
			clLike = 0
			mtTaken = 0
			mtLike = 0
			actTaken = 0
			actLike = 0
			mtTotal = 0
			actTotal = 0
			try:
				for c in cl:
					if c.statistic.currentTakenNumber:
						clTaken += c.statistic.currentTakenNumber
					if c.statistic.currentLikeNumber:
						clLike += c.statistic.currentLikeNumber
					for mt in c.material:
						if mt.statistic.currentTakenNumber:
							mtTaken += mt.statistic.currentTakenNumber
						if mt.statistic.currentLikeNumber:
							mtLike += mt.statistic.currentLikeNumber
							mtTotal += 1
					for act in c.action:
						if act.statistic.currentTakenNumber:
							actTaken += act.statistic.currentTakenNumber
						if act.statistic.currentLikeNumber:
							actLike += act.statistic.currentLikeNumber
							actTotal +=1
				print(mtTaken)
				print(mtLike)
				print(actTaken)
				print(actLike)
			except Exception as e:
				print(e)
# 			user=User.objects.get(username=str(request.user))
# 			print(user.id)
# 			student=Student.objects.get(user=user.id)
# 			print(student.id)
			progress = CurriculumnStudyProgress.objects(curriculumn=cl[0].id,student=student.id)
			is_joined = False
			if len(progress)>0:
				is_joined = True
			#comments = CommentPost.objects(post_id=vpost_id).all()
			#comments = cl.comments
			context = {	'cl':cl[0],'is_joined':is_joined,
						'user_id':request.user,
						'course_id':curriculum_id,
						'author':user.username,
						'is_mentor':is_mentor,
						'clTaken':clTaken,
						'clLike':clLike,
						'mtTaken':mtTaken,
						'mtLike':mtLike,
						'actTaken':actTaken,
						'actLike':actLike,
						'mtTotal':mtTotal,
						'actTotal':actTotal,
						'has_curriculum':has_curriculum,
						}
# 			return render(request, '/course-detail?course_id=' + curriculum_id+'&user_id=' + user_id, context)53833c3430635f163c51a5d5
			return HttpResponseRedirect('course-detail?course_id='+ curriculum_id +'&user_id='+user_id )
		else :
			comment = request.POST['txtComment']
			course_id = request.POST['hd_course_id']
			material_id = request.POST['hd_material_id']
			user_id = request.session['_auth_user_id']
			ur = request.user
			cmt = Comment()
			cmt.user = request.user
			cmt.content=comment
# 			cmt.save()
			cl = Curriculumn.objects.get(id=course_id)
			mt = Material.objects.get(id=material_id)
			mt.comment.append(cmt);
# 			mt.save()
# 			cl.save()
	# 		comments = CommentPost.objects(post_id=post_id).all()
			cl = Curriculumn.objects.get(id=course_id)
			context = {	'cl':cl,
						'user_id':request.user,
						'course_id':course_id
						}
			context.update(csrf(request))
			context.update(context_processors.user(request))
			return render_to_response("myapp/course-detail.html", context)
		