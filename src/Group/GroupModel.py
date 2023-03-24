from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


class Group(db.Model, Model):
	title = db.Column(db.String(60))
	description = db.Column(db.Text)

	image = relationship("Image", uselist=False)
	creator_id = db.Column(db.Integer, db.ForeignKey("user.id"))
	creator = relationship("User")
	users = relationship("User", secondary="group_invite")
