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
    region = db.Column(db.String(60), nullable=False)
    admin = db.Column(db.Boolean, default=False)

    email = relationship("Email", uselist=False)

    role_id = db.Column(db.Integer)
    image = relationship("Image", uselist=False)

    gender_id = db.Column(db.Integer, db.ForeignKey('gender.id'))
    gender = relationship("Gender")

    skills = relationship("Skill")
    user_contacts = relationship("UserContact")
    creation_date = db.Column(db.DateTime, default=datetime.utcnow())
    groups = relationship("Group", secondary="group_invite", secondaryjoin="and_(GroupInvite.group_id==Group.id, GroupInvite.confirmed==True)")
