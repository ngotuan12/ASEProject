from datetime import datetime

from mongoengine.document import Document
from mongoengine.fields import StringField, DateTimeField, ReferenceField, \
	ListField

from myapp.models.Comment import Comment
from myapp.models.MaterialType import MaterialType
from myapp.models.Unit import Unit


class Material(Document):
	published_date = DateTimeField(default=datetime.now)
	unit = ReferenceField(Unit)
	type = ReferenceField(MaterialType)
	name = StringField()
	url = StringField()
	code = StringField()
	description = StringField()
	comment = ListField(ReferenceField(Comment))
	meta = {
			'ordering': ['-published_date']
 }