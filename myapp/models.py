from datetime import datetime

from mongoengine import *
from mongoengine.django.auth import User


class BlogPost(Document):
	title = StringField()
	published_date = DateTimeField()
	user_id = ReferenceField(User)

	meta = {
		'ordering': ['-published_date']
	}
class UserLogin(Document):
	published_date = DateTimeField(default=datetime.now)
	use = ReferenceField(User)
	meta = {
		'ordering': ['-published_date']
	}