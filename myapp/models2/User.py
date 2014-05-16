from datetime import datetime

from mongoengine.django.auth import User
from mongoengine.document import Document
from mongoengine.fields import DateTimeField, ReferenceField


class User(Document):
	published_date = DateTimeField(default=datetime.now)
	use = ReferenceField(User)
	meta = {
		'ordering': ['-published_date']
	}
