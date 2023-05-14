
from src import db
from src.__Parents.Model import Model


class Complaint(db.Model, Model):
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	publication_id = db.Column(db.Integer, db.ForeignKey('publication.id'))
	vacancy_id = db.Column(db.Integer, db.ForeignKey('vacancy.id'))
