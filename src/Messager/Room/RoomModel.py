from sqlalchemy import desc
from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


class Room(db.Model, Model):
    users = relationship("User", secondary="room_user")
    messages = relationship("Message", order_by=desc("creation_date"))
