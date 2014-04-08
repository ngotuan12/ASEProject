'''
Created on Apr 3, 2014

@author: TuanNA
'''
from datetime import datetime

from mongoengine.django.auth import User
from mongoengine.document import Document
from mongoengine.fields import ReferenceField, StringField, DateTimeField,\
	ListField, EmbeddedDocumentField

from myapp.models.JobTitle import JobTitle
from myapp.models.Social import Social
from myapp.models.WorkField import WorkFeild


class UserProfile(Document):
	user_id = ReferenceField(User)
	user_type = StringField()
	job_title = ReferenceField(JobTitle)
	images = StringField()
	company = StringField()
	work_field = ReferenceField(WorkFeild)
	edu = ListField(StringField())
	skill =ListField(StringField())
	socials = ListField(EmbeddedDocumentField(Social))
	create_date = DateTimeField(default=datetime.now)
	status = int()
	about = StringField()
	meta = {
			'ordering': ['-create_date']
			}
