from mongoengine.django.auth import User
from mongoengine.document import Document
from mongoengine.fields import ReferenceField


class Student(Document):
	published_date = DateTimeField(default=datetime.now)
	user = ReferenceField(User)
	meta = {
		'ordering': ['-published_date']
	}
