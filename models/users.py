from config.dbconnect import db


class Users(db.Document):
    id = db.SequenceField()
    name = db.StringField(required=True)
    documentType = db.StringField(required=True, choices=['RG', 'CPF'])
    documentNumber = db.StringField(required=True)
    paymentMethod = db.StringField(required=True)
    paymentData = db.ListField(required=True)
