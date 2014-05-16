from datetime import datetime

from mongoengine.document import Document
from mongoengine.fields import StringField, ReferenceField, ListField, \
	DateTimeField

from myapp.models.Comment import Comment
from myapp.models.Curriculumn import Curriculumn


class Action(Document):
	published_date = DateTimeField(default=datetime.now)
	actionName = StringField()
	actionDescription = StringField()
	comment = ListField(ReferenceField(Comment))
	meta = {
		'ordering': ['-published_date']
	}
