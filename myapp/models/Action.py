from datetime import datetime

from mongoengine.document import Document
from mongoengine.fields import StringField, ReferenceField, ListField, \
	DateTimeField

from myapp.models.Comment import Comment
class Action(Document):
	published_date = DateTimeField(default=datetime.now)
	name = StringField()
	description = StringField()
	comment = ListField(ReferenceField(Comment))
	meta = {
		'ordering': ['-published_date']
	}
