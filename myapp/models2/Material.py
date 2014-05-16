from datetime import datetime

from mongoengine.document import Document
from mongoengine.fields import StringField, DateTimeField, ReferenceField

from myapp.models2.Curriculumn import Curriculumn
from myapp.models2 import Units
from myapp.models2 import MaterialType
from myapp.models2.Comment import Comment

class Material(Document):
	published_date = DateTimeField(default=datetime.now)
	curriculumsname = ReferenceField(Curriculumn)
	unit = ReferenceField(Units)
	materialtype = ReferenceField(MaterialType)
	materialname = StringField()
	materialURL = StringField()
	materialcode = StringField()
	comment = ListField(ReferenceField(Comment))
	meta = {
			'ordering': ['-published_date']
 }
