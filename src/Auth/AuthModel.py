from src import db
from src.__Parents.Model import Model


class Auth(Model, db.Model):
    user_id = db.Column(db.Integer, nullable=False)
    access_token = db.Column(db.String(320), nullable=False)
    # refresh_token = db.Column(db.String(320), nullable=False)

    def __init__(self, user_id: int):
        self.user_id = user_id
