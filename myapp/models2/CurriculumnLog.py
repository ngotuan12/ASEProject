from datetime import datetime

from mongoengine.document import Document
from mongoengine.fields import  DateTimeField, ReferenceField,IntField

from myapp.models2.Curriculumn import Curriculumn
from myapp.models2.User import User


class CurriculumnLog(Document):
	published_date = DateTimeField(default=datetime.now)
	curriculumn = ReferenceField(Curriculumn)
	like = IntField()
	user = ReferenceField(User)
	meta = {
			'ordering': ['-published_date']
 }
