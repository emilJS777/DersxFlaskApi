from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


class Rubric(Model, db.Model):
    title = db.Column(db.String(80), nullable=False)
    title_eng = db.Column(db.String(80), nullable=False)
    title_arm = db.Column(db.String(80), nullable=False)
    title_rus = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120))

    categories = relationship("Category")


