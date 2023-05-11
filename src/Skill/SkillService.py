from src.__Parents.Repository import Repository
from src.__Parents.Service import Service
from .ISkillRepo import ISkillRepo
from src.Category.ICategoryRepo import ICategoryRepo


class SkillService(Service, Repository):

    def __init__(self, skill_repository: ISkillRepo, category_repository: ICategoryRepo):
        self.skill_repository: ISkillRepo = skill_repository
        self.category_repository: ICategoryRepo = category_repository

    def create(self, body: dict) -> dict:
        categories = self.category_repository.get_all(ids=body['category_ids'])
        self.skill_repository.create(body=body, categories=categories)
        return self.response_created(msg_rus='умение создано', msg_arm='հմտությունը ստեղծված է', msg_eng='skill created')

    def update(self, skill_id: int, body: dict) -> dict:
        skill = self.skill_repository.get_by_id(skill_id=skill_id)
        categories = self.category_repository.get_all(ids=body['category_ids'])
        self.skill_repository.update(skill=skill, body=body, categories=categories)
        return self.response_updated(msg_rus='умение обновлен', msg_eng='skill created', msg_arm='հմտությունը թարմացվել է')

    def delete(self, skill_id: int) -> dict:
        skill = self.skill_repository.get_by_id(skill_id=skill_id)
        self.skill_repository.delete(skill=skill)
        return self.response_deleted(msg_rus='умение удален', msg_arm='հմտությունը ջնջված է', msg_eng='skill deleted')

    def get_by_id(self, skill_id: int) -> dict:
        skill = self.skill_repository.get_by_id(skill_id=skill_id)
        return self.response_ok({
            'id': skill.id,
            'tags': skill.tags,
            'rubric_id': skill.rubric_id,
            'categories': self.get_array_items(skill.categories)
        })

    def get_all(self, user_id: int) -> dict:
        skills = self.skill_repository.get_all(user_id=user_id)
        return self.response_ok([{
            'id': skill.id,
            'tags': skill.tags,
            'rubric': self.get_dict_items(skill.rubric),
            'categories': self.get_array_items(skill.categories)
        } for skill in skills])

