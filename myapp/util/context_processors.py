from myapp.models.Mentor import Mentor

def user(request):
	"""A context processor that adds the user to template context"""
	profile = {}
	is_mentor = False
	if (request.user.is_authenticated()==True) and(request.user is not None):
		try:
			isMentor = Mentor.objects.get(user=request.user)
			if len(isMentor):
				is_mentor = True
		except Exception as e:
			is_mentor = False
	return {
		'user': request.user,
		'profile':profile,
		'is_mentor':is_mentor
	}