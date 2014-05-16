from datetime import datetime

from mongoengine.document import Document
from mongoengine.fields import DateTimeField, ReferenceField,\
	StringField

from myapp.models2.Material import Material
from myapp.models2.Student import Student
from myapp.models2.Impression import Impression
from myapp.models2.ProgressType import ProgressType

class MaterialStudyProgress(Document):
	published_date = DateTimeField(default=datetime.now)	
	material = ReferenceField(Material)
	student = ReferenceField(Student)
	impression = ReferenceField(Impression)	
	progressType = ReferenceField(ProgressType)	
	description = StringField()	
	PlanStartDate = DateTimeField()
	PlanEndDate = DateTimeField()
	ActualStartDate = DateTimeField()
	ActualEndDate = DateTimeField()
	lastUpdate = DateTimeField()
	meta = {
			'ordering': ['-published_date']
 }
