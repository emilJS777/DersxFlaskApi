from sqlalchemy.orm import relationship

from src import db
from src.__Parents.Model import Model


class Email(db.Model, Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = relationship("User")
    address = db.Column(db.String(120), nullable=False)
    active = db.Column(db.Boolean, default=False)
    activation_code = db.Column(db.String(40))
