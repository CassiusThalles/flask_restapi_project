from config.dbconnect import db
from .cerditcard import CreditCard
from .virtualwallet import VirtualWallet


class Users(db.Document):
    id = db.SequenceField()
    name = db.StringField(required=True)
    documentType = db.StringField(required=True, choices=['RG', 'CPF'])
    documentNumber = db.StringField(required=True)
    paymentMethod = db.StringField(required=True)
    creditCard = db.EmbeddedDocumentField(CreditCard)
    virtualWallet = db.EmbeddedDocumentField(VirtualWallet)
