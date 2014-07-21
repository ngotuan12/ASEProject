'''
Created on Apr 3, 2014

@author: TuanNA
'''
from datetime import datetime

from mongoengine.django.auth import User
from mongoengine.document import Document
from mongoengine.fields import ReferenceField, StringField, DateTimeField,\
	FloatField


class CusDebit(Document):
	cus_id  = ReferenceField(User)
	month = DateTimeField(default=datetime.now)
	debit = FloatField()
	create_date = DateTimeField(default=datetime.now)
	loan_date = DateTimeField(default=datetime.now)
	status = FloatField()
	note = StringField()
	meta = {
			'ordering': ['-create_date']
			}