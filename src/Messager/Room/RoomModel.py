from sqlalchemy import desc
from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


class RoomUser(db.Model, Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    room_id = db.Column(db.Integer, db.ForeignKey("room.id"))


class Room(db.Model, Model):
    users = relationship("User", secondary="room_user")
    message = relationship("Message", order_by=desc("creation_date"), uselist=False)
