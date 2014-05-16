from datetime import datetime

from mongoengine.document import Document
from mongoengine.fields import DateTimeField, ReferenceField,IntField

from myapp.models2.Curriculumn import Curriculumn

class CurriculumsStaticAccumlate(Document):
	published_date = DateTimeField(default=datetime.now)
	curriculumn = ReferenceField(Curriculumn)
	currentLikeNumber = IntField()
	currentTakenNumber = IntField()
	lastUpdate = DateTimeField()
	meta = {
			'ordering': ['-published_date']
 }
