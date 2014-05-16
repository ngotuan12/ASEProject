from datetime import datetime

from mongoengine.document import Document
from mongoengine.fields import StringField, DateTimeField, ReferenceField, \
	ListField

from myapp.models.Comment import Comment
from myapp.models.Curriculumn import Curriculumn
from myapp.models.MaterialType import MaterialType
from myapp.models.Unit import Unit


class Material(Document):
	published_date = DateTimeField(default=datetime.now)
	unit = ReferenceField(Unit)
	materialtype = ReferenceField(MaterialType)
	materialname = StringField()
	materialURL = StringField()
	materialcode = StringField()
	comment = ListField(ReferenceField(Comment))
	meta = {
			'ordering': ['-published_date']
 }
