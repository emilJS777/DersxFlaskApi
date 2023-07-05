from src import db
from src.__Parents.Model import Model


class File(db.Model, Model):
    filename = db.Column(db.String(180), nullable=False)
    vacancy_offer_id = db.Column(db.Integer, db.ForeignKey("vacancy_offer.id"))
