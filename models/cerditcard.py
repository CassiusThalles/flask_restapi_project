from config.dbconnect import db


class CreditCard(db.Document):
    id = db.SequenceField()
    cardflag = db.StringField(required=True)
    cardnumber = db.IntField(required=True)
    expirationdata = db.DateTimeField(required=True)
    securitycode = db.IntField(required=True)
