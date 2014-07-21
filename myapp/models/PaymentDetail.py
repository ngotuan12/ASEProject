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
from myapp.models.Payment import Payment


class PaymentDetail(Document):
	payment_id = ReferenceField(Payment)
	cus_debit_id = ReferenceField(CusDebit)
	cus_id  = ReferenceField(User)
	create_date= DateTimeField(default=datetime.now)
	debit = FloatField()
	payment = FloatField()
	remain = FloatField()
	status = int()
	meta = {
			'ordering': ['-create_date']
			}