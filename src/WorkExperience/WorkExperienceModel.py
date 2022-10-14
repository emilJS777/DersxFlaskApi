from src import db
from src.__Parents.Model import Model


class WorkExperience(db.Model, Model):
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text)
    skills = db.Column(db.String(120))
    link = db.Column(db.String(420))

    date_start = db.Column(db.Date())
    date_end = db.Column(db.Date())

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
