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
# 		cl = Curriculumn.objects(mentor=mentor)
# 		mentor = Mentor.objects.get(user=re)
# 		mentor_id = '5375ce146c02298c9af00e00'
		user_id=request.GET['user_id']
		user = User.objects.get(id=user_id)
		mentor = Mentor.objects.get(user=user)
		cl = Curriculumn.objects(mentor=mentor)
# 		print(user.id)
# 		cl = Curriculumn.objects()
		context = {'user_id':user_id,'cl':cl,}
		return render(request,'myapp/studentview.html', context)