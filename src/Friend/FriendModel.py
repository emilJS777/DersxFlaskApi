from src import db
from src.__Parents.Model import Model


class Friend(db.Model, Model):
    user_1_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_2_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    creator_id = db.Column(db.Integer)
    confirmed = db.Column(db.Boolean, default=False)
