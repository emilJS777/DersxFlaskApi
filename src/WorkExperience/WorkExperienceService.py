from src.__Parents.Repository import Repository
from src.__Parents.Service import Service
from .IWorkExperienceRepo import IWorkExperienceRepo
from flask import g


class WorkExperienceService(Service, Repository):

    def __init__(self, work_experience_repository: IWorkExperienceRepo):
        self.work_experience_repository: IWorkExperienceRepo = work_experience_repository

    def create(self, body: dict) -> dict:
        self.work_experience_repository.create(body)
        return self.response_created('опыт работы было создано')

    def update(self, work_experience_id: int, body: dict) -> dict:
        work_experience = self.work_experience_repository.get_by_id(work_experience_id=work_experience_id)
        if not work_experience or not work_experience.user_id == g.user_id:
            return self.response_not_found('опыт работы не найдено ')

        self.work_experience_repository.update(work_experience=work_experience, body=body)
        return self.response_updated('опыт работы было обновлено')

    def delete(self, work_experience_id: int) -> dict:
        work_experience = self.work_experience_repository.get_by_id(work_experience_id=work_experience_id)
        if not work_experience or not work_experience.user_id == g.user_id:
            return self.response_not_found('опыт работы не найдено ')

        self.work_experience_repository.delete(work_experience)
        return self.response_deleted('опыт работы было удалено')

    def get_by_id(self, work_experience_id: int) -> dict:
        work_experience = self.work_experience_repository.get_by_id(work_experience_id=work_experience_id)
        if not work_experience:
            return self.response_not_found('опыт работы не найдено ')

        return self.response_ok(self.get_dict_items(work_experience))

    def get_all(self, user_id: int) -> dict:
        work_experiences = self.work_experience_repository.get_all(user_id=user_id)
        return self.response_ok(self.get_array_items(work_experiences))
