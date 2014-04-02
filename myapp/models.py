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
class CommentPost(Document):
	post_id=ReferenceField(MentorPost)
	create_date = DateTimeField(default=datetime.now)
	user_id = ReferenceField(User)
	content = StringField()
	meta = {
			'ordering': ['-published_date']
 }
class UserType(Document):
	user_type= StringField()
	create_date = DateTimeField(default=datetime.now)
	status = int()
	meta = {
			'ordering': ['-create_date']
 }
class JobTitle(Document):
	code= StringField()
	name= StringField()
	create_date = DateTimeField(default=datetime.now)
	status = int()
class WorkFeild(Document):
	code= StringField(max_length=5)
	type_name = StringField()
	status = int()
class UserProfile(Document):
	user_id = ReferenceField(User)	
	user_type = StringField()
	job_title = ReferenceField(JobTitle)
	images = StringField(default="images/photos/user.png")
	company = StringField()
	work_field = ReferenceField(WorkFeild)
	edu = StringField()
	skill = StringField()
	create_date = DateTimeField(default=datetime.now)
	status = int()
	about = StringField()
	meta = {
			'ordering': ['-published_date']
			}
	