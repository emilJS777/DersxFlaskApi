from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


class CompanyUser(db.Model, Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    company_id = db.Column(db.Integer, db.ForeignKey("company.id"))


class CompanyRubric(db.Model, Model):
    rubric_id = db.Column(db.Integer, db.ForeignKey("rubric.id"))
    company_id = db.Column(db.Integer, db.ForeignKey("company.id"))


class Company(db.Model, Model):
    title = db.Column(db.String(60), nullable=False)
    short_description = db.Column(db.String(400), nullable=False)
    long_description = db.Column(db.Text, nullable=False)
    image = relationship("Image", uselist=False)

    creator_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    creator = relationship("User")

    rubrics = relationship("Rubric", secondary="company_rubric")
    users = relationship("User", secondary="company_user")

