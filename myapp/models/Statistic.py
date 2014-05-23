from datetime import datetime

from mongoengine.document import Document
from mongoengine.fields import  DateTimeField, IntField


class Statistic(Document):
	create_date = DateTimeField(default=datetime.now)
	currentLikeNumber = IntField()
	currentTakenNumber = IntField()
	lastUpdate = DateTimeField()
	meta = {
			'ordering': ['-published_date']
 }
