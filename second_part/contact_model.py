from mongoengine import Document, connect
from mongoengine.fields import (
    StringField,
    EmailField,
    BooleanField
)


connect(db='Homework08_part2',
        host='mongodb+srv://Homework08:Homework08@homework08.mbxw22h.mongodb.net/'
             f'?retryWrites=true&w=majority&appName=Homework08')


class Contact(Document):
    fullname = StringField(max_length=30, required=True)
    email = EmailField(required=True)
    mailed = BooleanField(default=False)