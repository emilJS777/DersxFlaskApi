from src import db
from src.__Parents.Model import Model
from flask import request


class PaymentInterval(db.Model, Model):
    title = db.Column(db.String(20), nullable=False)
    title_eng = db.Column(db.String(20), nullable=False)
    title_arm = db.Column(db.String(20), nullable=False)
    title_rus = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(60))
    price = db.Column(db.Boolean, default=False)

