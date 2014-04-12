'''
Created on Apr 3, 2014

@author: TuanNA
'''
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from myapp.models import MentorPost


@login_required(login_url='/signin')
def index(request):
	posts = MentorPost.objects
	user_type = ""
	try:
		user_type = request.session['user_type']
	except Exception:
		user_type = ""
	context = {'posts':posts,'user_type':user_type,'user_id':request.user,}
	return render(request,'myapp/index.html', context)