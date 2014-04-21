'''
Created on Apr 3, 2014

@author: TuanNA
'''
from datetime import datetime

from mongoengine.django.auth import User
from mongoengine.document import Document
from mongoengine.fields import StringField, DateTimeField, ReferenceField, ListField

from myapp.models.CommentPost import CommentPost


class MentorPost(Document):
	title = StringField()
	published_date = DateTimeField(default=datetime.now)
	from_date = DateTimeField(default=datetime.now)
	to_date = DateTimeField(default=datetime.now)
	place = StringField()
	user_id = ReferenceField(User)
	videolink = StringField()
	imagelink = StringField()
	amazonlink= StringField()
	content = StringField()
	post_type=StringField(default="0")
	status=StringField(default="1")
	comments=ListField(ReferenceField(CommentPost))
	meta = {
			'ordering': ['-published_date']
 }
