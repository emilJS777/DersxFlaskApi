from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model
from datetime import datetime
from sqlalchemy.sql import func


class VacancyComment(db.Model, Model):
    text = db.Column(db.String(1500), nullable=False)
    vacancy_id = db.Column(db.Integer, db.ForeignKey("vacancy.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = relationship("User")
    creation_date = db.Column(db.DateTime(timezone=True), server_default=func.now())
