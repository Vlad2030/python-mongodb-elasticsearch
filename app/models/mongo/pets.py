from datetime import datetime

from mongoengine.document import Document
from mongoengine.fields import (
    DateTimeField,
    IntField,
    ObjectIdField,
    StringField,
    ObjectId
)


class Pets(Document):
    id = ObjectIdField(required=True, primary_key=True)
    name = StringField(min_length=1, max_length=256)
    age = IntField(min_value=1, max_value=256)
    type = StringField(min_length=1, max_length=256)
    created_at = DateTimeField(default=datetime.now)
