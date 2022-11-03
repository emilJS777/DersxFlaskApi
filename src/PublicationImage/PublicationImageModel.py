from src import db
from src.__Parents.Model import Model


class PublicationImage(db.Model, Model):
    filename = db.Column(db.String(120), nullable=False)
    publication_id = db.Column(db.Integer, db.ForeignKey("publication.id"))
