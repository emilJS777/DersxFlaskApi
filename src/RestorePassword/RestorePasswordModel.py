from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


class RestorePassword(db.Model, Model):
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	user = relationship("User")
	security_code = db.Column(db.String(40), unique=True)