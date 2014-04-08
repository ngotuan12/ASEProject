'''
Created on Apr 3, 2014

@author: TuanNA
'''
from mongoengine.document import EmbeddedDocument
from mongoengine.fields import StringField


class Social(EmbeddedDocument):
	name=StringField()
	type=StringField(max_length=2)
	status=StringField(default=1)
	icon=StringField()