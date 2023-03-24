from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


class GroupInvite(db.Model, Model):
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
	group = relationship("Group")
	confirmed = db.Column(db.Boolean, default=True)

