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
class MentorPost(Document):
	title = StringField()
	published_date = DateTimeField(default=datetime.now)
	user_id = ReferenceField(User)
	imagelink = StringField()
	content = StringField()
	meta = {
			'ordering': ['-published_date']
 }
class CommentPost(Document):
	post_id=ReferenceField(MentorPost)
	create_date = DateTimeField(default=datetime.now)
	user_id = ReferenceField(User)
	content = StringField()
	meta = {
			'ordering': ['-published_date']
 }
class UserType(Document):	
	type_name= StringField()
	create_date = DateTimeField(default=datetime.now)
	status = int(2)
	meta = {
			'ordering': ['-create_date']
 }
class workfield(Document):	
	workfield= StringField()
	create_date = DateTimeField(default=datetime.now)
	status = int(2)
	meta = {
			'ordering': ['-create_date']
 }
class UserProfile(Document):
	user_id = ReferenceField(User)
	imagelink = StringField()
	user_type = ReferenceField(UserType)
	job_title = StringField()
	company = StringField()
	work_field = ReferenceField(workfield)
	edu = StringField()
	skill = StringField()
	create_date = DateTimeField(default=datetime.now)
	status = int(2)
	meta = {
			'ordering': ['-published_date']
 }
	