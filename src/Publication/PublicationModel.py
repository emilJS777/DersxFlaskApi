from sqlalchemy import func
from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model
from datetime import datetime


class Publication(db.Model, Model):
    description = db.Column(db.Text, nullable=False)
    image = relationship("PublicationImage", uselist=False)

    creator_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    creator = relationship("User")

    creation_date = db.Column(db.DateTime(timezone=True), default=func.now())