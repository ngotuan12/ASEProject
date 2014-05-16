from datetime import datetime

from mongoengine.document import Document
from mongoengine.fields import StringField, DateTimeField, ReferenceField, IntField, \
	ListField

from myapp.models.Category import Category
from myapp.models.Comment import Comment
from myapp.models.Mentor import Mentor
from myapp.models.Unit import Unit


class Curriculumn(Document):
	published_date = DateTimeField(default=datetime.now)
	curriculumnname = StringField()
	duration = IntField()
	duration_type = StringField()
	category= ReferenceField(Category)
	from_date = DateTimeField(default=datetime.now)
	to_date = DateTimeField(default=datetime.now)
	description = StringField()
	mentor = ReferenceField(Mentor)
	units = ListField(ReferenceField(Unit))
	comments = ListField(ReferenceField(Comment))
	meta = {
				'ordering': ['-mentor'],
				'ordering': ['-comments'],
				'ordering': ['-units']
			}
