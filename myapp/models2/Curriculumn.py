from datetime import datetime

from mongoengine.document import Document
from mongoengine.fields import StringField, DateTimeField, ReferenceField, IntField

from myapp.models2.Category import Category
from myapp.models2.Comment import Comment

class Curriculumn(Document):
	published_date = DateTimeField(default=datetime.now)
	curriculumnname = StringField()
	duration = IntField()
	category= ReferenceField(Category)
	from_date = DateTimeField(default=datetime.now)
	to_date = DateTimeField(default=datetime.now)
	description = StringField()
	mentor = ReferenceField(Mentor)
	units = ListField(ReferenceField(Unit))
	comment = ListField(ReferenceField(Comment))
	meta = {
			'ordering': ['-published_date']
 }
