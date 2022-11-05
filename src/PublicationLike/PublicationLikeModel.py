from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


class PublicationLike(db.Model, Model):
    publication_id = db.Column(db.Integer, db.ForeignKey("publication.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
