'''
Created on Apr 3, 2014

@author: TuanNA
'''
from datetime import datetime

from mongoengine.django.auth import User
from mongoengine.document import Document
from mongoengine.fields import ReferenceField, DateTimeField,\
	FloatField

from myapp.models.CusDebit import CusDebit


class CusDebitDetail(Document):
	cus_id  = ReferenceField(User)
	cus_debit_id  = ReferenceField(CusDebit)
	from_date= DateTimeField(default=datetime.now)
	to_date= DateTimeField(default=datetime.now)
	rate = FloatField()
	start_cycle = FloatField()
	amount = FloatField()
	payment = FloatField()
	end_cycle = FloatField()
	debit = FloatField()
	status = FloatField()
	create_date= DateTimeField(default=datetime.now)
	is_current_month = FloatField()
	meta = {
			'ordering': ['-create_date']
			}