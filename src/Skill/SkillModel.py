from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


class SkillCategory(Model, db.Model):
    skill_id = db.Column(db.Integer, db.ForeignKey("skill.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))


class Skill(Model, db.Model):
    tags = db.Column(db.String(120), nullable=False)

    rubric_id = db.Column(db.Integer, db.ForeignKey("rubric.id"))
    rubric = relationship("Rubric")

    categories = relationship("Category", secondary="skill_category")
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
