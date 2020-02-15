from config.dbconnect import db


class Sellers(db.Document):
    id = db.SequenceField()
    company_name = db.StringField(required=True)
    cnpj = db.StringField(requirsed=True)
    acceptedPaymentMethods = db.ListField(required=True)