'''
Created on Apr 3, 2014

@author: ducdienpt
'''
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from myapp.models import UserProfile, Mentor


def index(request):
	lisUserProfile = {}
	c = {'lisUserProfile':lisUserProfile,}
	if request.method == 'GET':
		return render(request, 'myapp/become-mentor.html', c)
	elif request.method == 'POST':
		profile = UserProfile.objects.get(user_id=request.user)
		print(request.user)
		profile.is_mentor = True
# 		profile.save()
		mentor = Mentor()
		mentor.user = request.user
# 		mentor.save()
		return HttpResponseRedirect("/home")
# 	return render(request, 'myapp/become-mentor.html', c)