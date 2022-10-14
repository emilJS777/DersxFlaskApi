from src import db
from src.__Parents.Model import Model


class UserImage(db.Model, Model):
    filename = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
