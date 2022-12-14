from src import db
from src.__Parents.Model import Model


class RoomUser(db.Model, Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    room_id = db.Column(db.Integer, db.ForeignKey("room.id"))
