from mongoengine.document import Document
from mongoengine.fields import StringField, ReferenceField, IntField


class Category(Document):
	categoryName = StringField()
	parentCategory = StringField()
	currentCategoryTree = StringField()
	showpiority = IntField()
	meta = {
	}
