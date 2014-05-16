from mongoengine.document import Document
from mongoengine.fields import StringField, ReferenceField


class Category(Document):
	categoryName = StringField()
	parentCategory = ReferenceField(Category)
	currentCategoryTree = StringField()
	showpiority = IntField()
	meta = {
		'ordering': ['-published_date']
	}
