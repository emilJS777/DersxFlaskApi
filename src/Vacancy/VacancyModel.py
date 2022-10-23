from datetime import datetime
from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


class VacancyCategory(db.Model, Model):
    vacancy_id = db.Column(db.Integer, db.ForeignKey('vacancy.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))


class Vacancy(db.Model, Model):
    title = db.Column(db.String(50), nullable=False)
    short_description = db.Column(db.String(600), nullable=False)
    long_description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Numeric)
    rubric_id = db.Column(db.Integer, db.ForeignKey('rubric.id'))
    rubric = relationship("Rubric")
    categories = relationship("Category", secondary="vacancy_category")

    payment_interval_id = db.Column(db.Integer, db.ForeignKey('payment_interval.id'))
    payment_interval = relationship("PaymentInterval")

    vacancy_offers = relationship("VacancyOffer")
    vacancy_comments = relationship("VacancyComment")
    creation_date = db.Column(db.DateTime, default=datetime.utcnow())
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    creator = relationship("User")

