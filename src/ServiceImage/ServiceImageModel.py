from src import db
from src.__Parents.Model import Model


class ServiceImage(db.Model, Model):
    filename = db.Column(db.String(120), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey("service.id"))
