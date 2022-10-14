from src import db
from src.__Parents.Model import Model


class Category(Model, db.Model):
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120))

    rubric_id = db.Column(db.Integer, db.ForeignKey("rubric.id"))




