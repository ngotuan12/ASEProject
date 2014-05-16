from datetime import datetime

from mongoengine.document import Document
from mongoengine.fields import DateTimeField, StringField


class Units(Document):
	published_date = DateTimeField(default=datetime.now)
	unitName = StringField()
	meta = {
		'ordering': ['-published_date']
	}
