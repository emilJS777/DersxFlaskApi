from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model
from datetime import datetime


class ServiceCategory(db.Model, Model):
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))


class Service(db.Model, Model):
    title = db.Column(db.String(50), nullable=False)
    short_description = db.Column(db.String(400), nullable=False)
    long_description = db.Column(db.Text)

    rubric_id = db.Column(db.Integer, db.ForeignKey("rubric.id"))
    rubric = relationship("Rubric")
    categories = relationship("Category", secondary="service_category")
    image = relationship("ServiceImage", uselist=False)

    payment_interval_id = db.Column(db.Integer, db.ForeignKey('payment_interval.id'))
    payment_interval = relationship("PaymentInterval")
    price = db.Column(db.Numeric)

    creator_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    creator = relationship("User")
    creation_date = db.Column(db.DateTime, default=datetime.utcnow())

