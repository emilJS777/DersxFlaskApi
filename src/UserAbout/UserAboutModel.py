from src import db
from src.__Parents.Model import Model


class UserAbout(db.Model, Model):
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
