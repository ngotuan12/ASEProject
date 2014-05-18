'''
Created on Apr 3, 2014

@author: ducdienpt
'''
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from myapp.models import UserProfile, Mentor


@login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':
		return render(request, 'myapp/become-mentor.html', {})
	elif request.method == 'POST':
		profile = UserProfile.objects.get(user_id=request.user)
		profile.is_mentor = True
		profile.save()
		mentor = Mentor()
		mentor.user = request.user
		mentor.save()
		return HttpResponseRedirect('/studentview?user_id='+str(request.user.id))
# 	return render(request, 'myapp/become-mentor.html', c)