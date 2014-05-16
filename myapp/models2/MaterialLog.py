from datetime import datetime

from mongoengine.document import Document
from mongoengine.fields import  DateTimeField, ReferenceField,IntField

from myapp.models2.Material import Material
from myapp.models2.User import User


class CurriculumsLog(Document):
	published_date = DateTimeField(default=datetime.now)
	material = ReferenceField(Material)
	Like = IntField()
	user = ReferenceField(User)
	meta = {
			'ordering': ['-published_date']
 }
