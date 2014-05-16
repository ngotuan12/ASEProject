from mongoengine.document import Document
from mongoengine.fields import StringField


class Impression(Document):
	imdescription = StringField()
	showpiority = IntField()
	meta = {
		'ordering': ['-published_date']
	}
