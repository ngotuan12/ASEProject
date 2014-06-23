from requests import request, HTTPError
from myapp.models.UserProfile import UserProfile

def save_profile_picture(strategy, user, response, details,is_new=False,*args,**kwargs):

	if strategy.backend.name == 'facebook':
		url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
	
	if strategy.backend.name == 'twitter':
		url = response.get('profile_image_url', '').replace('_normal', '')
	
	if strategy.backend.name == 'google' and "picture" in response:
		url = response["picture"]
	
	
	try:
		if url:
			thisprofile = UserProfile.objects(user_id=user)
			if len(thisprofile) == 0:
				upro = UserProfile()
				upro.user_id = user
				upro.images = url
				upro.save()
	except HTTPError:
		pass
	