from myapp.models.UserProfile import UserProfile


def user(request):
	"""A context processor that adds the user to template context"""
	profile = {}
	if (request.user.is_authenticated()==True) and(request.user is not None):
		profile = UserProfile.objects.get(user_id=request.user)
	return {
		'user': request.user,
		'profile':profile
	}