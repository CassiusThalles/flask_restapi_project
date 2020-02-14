from mongoengine import *
from config.dbconnect import myconnect


class Users(Document):
    id = SequenceField()
    name = StringField(required=True)
    documentType = StringField(required=True, choices=['RG', 'CPF'])
    documentNumber = StringField(required=True)