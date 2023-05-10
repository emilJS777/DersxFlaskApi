from src import db
from src.__Parents.Model import Model


class Gender(db.Model, Model):
    title = db.Column(db.String(10), nullable=False)
    title_eng = db.Column(db.String(10), nullable=False)
    title_arm = db.Column(db.String(10), nullable=False)
    title_rus = db.Column(db.String(10), nullable=False)

