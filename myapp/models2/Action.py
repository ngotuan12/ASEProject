from mongoengine.document import Document
from mongoengine.fields import StringField, ReferenceField, ListField

from myapp.models2.Comment import Comment

class Action(Document):
	published_date = DateTimeField(default=datetime.now)
	curriculums = ReferenceField(Curriculums)
	actionName = StringField()
	actionDescription = StringField()
	comment = ListField(ReferenceField(Comment))
	meta = {
		'ordering': ['-published_date']
	}
