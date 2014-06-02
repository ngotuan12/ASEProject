from datetime import datetime

from mongoengine.document import Document
from mongoengine.fields import  DateTimeField, IntField, StringField


class Statistic(Document):
	create_date = DateTimeField(default=datetime.now)
	currentLikeNumber = IntField()
	currentTakenNumber = IntField()
	lastUpdate = DateTimeField()
	type =StringField()
	meta = {
			'ordering': ['-published_date']
}
