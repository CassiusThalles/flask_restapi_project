from config.dbconnect import db


class VirtualWallet(db.Document):
    id = db.SequenceField()
    currentmoney = db.FloatField(min_value=0.0, required=True)
    lastapport = db.DateTimeField()
