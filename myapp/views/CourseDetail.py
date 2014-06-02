'''
Created on Apr 3, 2014

@author: TuanNA
'''
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from mongoengine.django.auth import User

from myapp.models import Comment, Student, Impression
from myapp.models.CommentPost import CommentPost
from myapp.models.Curriculumn import Curriculumn
from myapp.models.CurriculumnLog import CurriculumnLog
from myapp.models.CurriculumnStudyProgress import CurriculumnStudyProgress
from myapp.models.Material import Material
from myapp.models.MentorPost import MentorPost
from myapp.models.ProgressType import ProgressType
from myapp.util import context_processors


#@login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':
		vCourse_id = request.GET['course_id']
		author_id=request.GET['user_id']
		author = User.objects.get(id=author_id)
		cl = Curriculumn.objects(id=vCourse_id)
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
		try :
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
		user=User.objects.get(username=str(request.user))
		print(user.id)
		student=Student.objects.get(user=user.id)
		print(student.id)
		progress = CurriculumnStudyProgress.objects(curriculumn=cl[0].id,student=student.id)
		is_joined = False
		if len(progress)>0:
			is_joined = True
		#comments = CommentPost.objects(post_id=vpost_id).all()
		#comments = cl.comments
		context = {	'cl':cl[0],'is_joined':is_joined,
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
		print(request.POST['posttype'])
		if request.POST['posttype']== "frmJoincourse":
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
		elif request.POST['posttype']== "likeMaterial":
			print('ok')
		else:
			comment = request.POST['txtComment']
			course_id = request.POST['hd_course_id']
			material_id = request.POST['hd_material_id']
			user_id = request.session['_auth_user_id']
			ur = request.user
			cmt = Comment()
			cmt.user = request.user
			cmt.content=comment
			cmt.save()
			cl = Curriculumn.objects.get(id=course_id)
			mt = Material.objects.get(id=material_id)
			mt.comment.append(cmt);
			mt.save()
			cl.save()
	# 		comments = CommentPost.objects(post_id=post_id).all()
			cl = Curriculumn.objects.get(id=course_id)
			context = {	'cl':cl,
						'user_id':request.user,
						'course_id':course_id
						}
			context.update(csrf(request))
			context.update(context_processors.user(request))
			return render_to_response("myapp/course-detail.html", context)