from requests import request, HTTPError
from myapp.models.UserProfile import UserProfile
import json

def save_profile_picture(strategy, user, response, details,is_new=False,*args,**kwargs):

	if strategy.backend.name == 'facebook':
		url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
	else:
		url = ""
	
	if strategy.backend.name == 'twitter':
		url = response.get('profile_image_url', '').replace('_normal', '')
	else:
		url = ""
	
	if strategy.backend.name == 'google' and "image" in response:
		resJSON = json.loads(response)
		inimgtag = resJSON['image']
		url = inimgtag['url']
	else:
		url = ""
	
	try:
		if url:
			try:
				thisprofile = UserProfile.objects(user_id=user)
				#ThaiNN Please review this code
				if len(thisprofile) == 0:
					upro = UserProfile()
					upro.user_id = user
					upro.images = url
					upro.save()
			except Exception as e:
					upro = UserProfile()
					upro.user_id = user
					upro.images = url
					upro.save()
					print(e)
	except HTTPError:
		pass