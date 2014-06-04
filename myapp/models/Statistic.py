from datetime import datetime

from mongoengine.document import Document
from mongoengine.fields import  DateTimeField, IntField, StringField,\
	ReferenceField, ListField

from myapp.models.StatisticDetail import StatisticDetail


class Statistic(Document):
	create_date = DateTimeField(default=datetime.now)
	currentLikeNumber = IntField()
	currentTakenNumber = IntField()
	statistic_detail = ListField(ReferenceField(StatisticDetail))
	lastUpdate = DateTimeField()
	type =StringField()
	meta = {
			'ordering': ['-create_date']
}
