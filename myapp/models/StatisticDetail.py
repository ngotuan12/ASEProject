
from datetime import datetime

from mongoengine.django.auth import User
from mongoengine.document import Document
from mongoengine.fields import  DateTimeField,ReferenceField, StringField


class StatisticDetail(Document):
	create_date = DateTimeField(default=datetime.now)
	like_user = ReferenceField(User)
	status = StringField(default='0')
	meta = {
			'ordering': ['-create_date']
}
