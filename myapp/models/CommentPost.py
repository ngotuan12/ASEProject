'''
Created on Apr 3, 2014

@author: TuanNA
'''
from datetime import datetime

from mongoengine.django.auth import User
from mongoengine.document import Document
from mongoengine.fields import ReferenceField, DateTimeField, StringField

from myapp.models.MentorPost import MentorPost


class CommentPost(Document):
	post_id=ReferenceField(MentorPost)
	create_date = DateTimeField(default=datetime.now)
	user_id = ReferenceField(User)
	content = StringField()
	meta = {
			'ordering': ['-published_date']
 }
