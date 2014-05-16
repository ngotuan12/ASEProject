from datetime import datetime

from mongoengine.document import Document
from mongoengine.fields import  DateTimeField, ReferenceField,IntField

from myapp.models2.Action import Action
from myapp.models2.User import User


class ActionLog(Document):
	published_date = DateTimeField(default=datetime.now)
	action = ReferenceField(Action)
	like = IntField()
	user = ReferenceField(User)
	meta = {
			'ordering': ['-published_date']
 }
