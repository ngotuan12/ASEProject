'''
Created on Apr 3, 2014

@author: TuanNA
'''
from datetime import datetime

from mongoengine.django.auth import User
from mongoengine.document import Document
from mongoengine.fields import StringField, DateTimeField, ReferenceField


class MentorPost(Document):
	title = StringField()
	published_date = DateTimeField(default=datetime.now)
	from_date = DateTimeField(default=datetime.now)
	to_date = DateTimeField(default=datetime.now)
	user_id = ReferenceField(User)
	imagelink = StringField()
	amazonlink= StringField()
	content = StringField()
	is_lecture=StringField(default=0)
	status=StringField(default=1)
	meta = {
			'ordering': ['-published_date']
 }
