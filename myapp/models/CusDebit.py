'''
Created on Apr 3, 2014

@author: TuanNA
'''
from datetime import datetime

from mongoengine.document import Document
from mongoengine.fields import ReferenceField, StringField, DateTimeField,\
	FloatField

from myapp.models.Customer import Customer
from myapp.models.LoanType import LoanType


class CusDebit(Document):
	cus_id  = ReferenceField(Customer)
	loan_type  = ReferenceField(LoanType)
	month = DateTimeField(default=datetime.now)
	debit = FloatField()
	total_debit = FloatField()
	payment = FloatField()
	create_date = DateTimeField(default=datetime.now)
	loan_date = DateTimeField(default=datetime.now)
	status = FloatField()
	note = StringField()
	meta = {
			'ordering': ['-create_date']
			}