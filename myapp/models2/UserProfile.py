from datetime import datetime

from mongoengine.django.auth import User
from mongoengine.document import Document
from mongoengine.fields import ReferenceField, StringField, DateTimeField,\
	ListField, IntField

from myapp.models.JobTitle import JobTitle
from myapp.models.WorkField import WorkFeild


class UserProfile(Document):
	user = ReferenceField(User)
	job_title = ReferenceField(JobTitle)
	images = StringField()
	company = StringField()
	work_field = ReferenceField(WorkFeild)
	edu = ListField(StringField())
	skill =ListField(StringField())
	create_date = DateTimeField(default=datetime.now)
	status = IntField()
	about = StringField()
	meta = {
			'ordering': ['-create_date']
			}
