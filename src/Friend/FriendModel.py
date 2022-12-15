from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


class Friend(db.Model, Model):
    users = relationship("User")
