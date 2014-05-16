from datetime import datetime

from mongoengine.document import Document
from mongoengine.fields import DateTimeField, ReferenceField,\
	StringField

from myapp.models2.Curriculumn import Curriculumn
from myapp.models2.Student import Student
from myapp.models2.Impression import Impression


class CurriculumsStudyLog(Document):
	published_date = DateTimeField(default=datetime.now)
	curriculumn = ReferenceField(Curriculumn)
	student = ReferenceField(Student)
	impression = ReferenceField(Impression)	
	progressType = ReferenceField(ProgressType)
	description = StringField()	
	meta = {
			'ordering': ['-published_date']
 }
