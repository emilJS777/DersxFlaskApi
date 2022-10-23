from sqlalchemy import func
from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


class VacancyOffer(db.Model, Model):
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Numeric(8, 2))

    payment_interval_id = db.Column(db.Integer, db.ForeignKey("payment_interval.id"))
    payment_interval = relationship("PaymentInterval")

    creation_date = db.Column(db.DateTime(timezone=True), server_default=func.now())

    vacancy_id = db.Column(db.Integer, db.ForeignKey("vacancy.id"))
    vacancy = relationship("Vacancy")

    creator_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    creator = relationship("User")
