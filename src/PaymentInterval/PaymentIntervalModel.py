from src import db
from src.__Parents.Model import Model


class PaymentInterval(db.Model, Model):
    title = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(60))
