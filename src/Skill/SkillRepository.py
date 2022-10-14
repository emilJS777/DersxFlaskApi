from src.Skill.ISkillRepo import ISkillRepo
from .SkillModel import Skill
from flask import g


class SkillRepository(ISkillRepo):
    def create(self, body: dict, categories: list):
        skill: Skill = Skill()
        skill.tags = body['tags']
        skill.rubric_id = body['rubric_id']
        skill.categories = categories
        skill.user_id = g.user_id
        skill.save_db()

    def delete(self, skill: Skill):
        skill.categories = []
        skill.update_db()
        skill.delete_db()

    def update(self, skill: Skill, body: dict, categories: list):
        skill.tags = body['tags']
        skill.rubric_id = body['rubric_id']
        skill.categories = categories
        skill.update_db()

    def get_by_id(self, skill_id: int) -> Skill:
        skill: Skill = Skill.query.filter_by(id=skill_id).first()
        return skill

    def get_all(self, user_id: int) -> list[Skill]:
        skills: list[Skill] = Skill.query.filter_by(user_id=user_id).all()
        return skills
