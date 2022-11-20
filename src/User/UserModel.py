from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model
from datetime import datetime


class User(Model, db.Model):
    name = db.Column(db.String(60), nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    date_birth = db.Column(db.Date(), nullable=False)
    email_address = db.Column(db.String(120), nullable=False)

    role_id = db.Column(db.Integer)
    # image_path = db.Column(db.String(120))
    image = relationship("Image", uselist=False)

    gender_id = db.Column(db.Integer, db.ForeignKey('gender.id'))
    gender = relationship("Gender")

    skills = relationship("Skill")
    user_contacts = relationship("UserContact")
    creation_date = db.Column(db.DateTime, default=datetime.utcnow())
