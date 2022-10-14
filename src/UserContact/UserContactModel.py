from src import db
from src.__Parents.Model import Model


class UserContact(db.Model, Model):
    type = db.Column(db.String(40), nullable=False)
    information = db.Column(db.String(120), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
