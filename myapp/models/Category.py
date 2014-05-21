from mongoengine.document import Document
from mongoengine.fields import StringField, IntField ,ReferenceField



class Category(Document):
	categoryName = StringField()
	parentCategory = ReferenceField('self', required=False)
	currentCategoryTree = StringField()
	showpiority = IntField()
	meta = {
	}
