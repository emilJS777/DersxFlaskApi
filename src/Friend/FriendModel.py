from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


class Friend(db.Model, Model):
    user_1_id = db.Column(db.Integer)
    user_2_id = db.Column(db.Integer)
    creator_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    creator = relationship("User")
    confirmed = db.Column(db.Boolean, default=False)
