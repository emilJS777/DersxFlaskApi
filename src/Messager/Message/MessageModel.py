from sqlalchemy import func
from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


class Message(db.Model, Model):
    text = db.Column(db.Text, nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey("room.id"))

    creator_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    creator = relationship("User")
    creation_date = db.Column(db.DateTime(timezone=True), default=func.now())