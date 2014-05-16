from mongoengine.document import Document
from mongoengine.fields import StringField


class ProgressType(Document):
	progressName = StringField()
	progressDescription = StringField()
	rate = IntField()
	meta = {
		'ordering': ['-published_date']
	}
