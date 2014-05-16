from datetime import datetime

from mongoengine.document import Document
from mongoengine.fields import  DateTimeField, ReferenceField,IntField

from myapp.models2.Material import Material


class ActionStaticAccumlated(Document):
	published_date = DateTimeField(default=datetime.now)
	material = ReferenceField(Material)
	currentLikeNumber = IntField()
	currentTakenNumber = IntField()
	lastUpdate = DateTimeField()
	meta = {
			'ordering': ['-published_date']
 }
