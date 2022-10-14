from src.__Parents.Repository import Repository
from src.__Parents.Service import Service
from .IUserAboutRepo import IUserAboutRepo
from flask import g


class UserAboutService(Service, Repository):

    def __init__(self, user_about_repository: IUserAboutRepo):
        self.user_about_repository: IUserAboutRepo = user_about_repository

    def create(self, body: dict) -> dict:
        self.user_about_repository.create(body)
        return self.response_created('описание о вас создано')

    def update(self, user_about_id: int, body: dict) -> dict:
        user_about = self.user_about_repository.get_by_id(user_about_id)
        if not user_about or not user_about.user_id == g.user_id:
            return self.response_not_found('описание о вас не найдено')
        self.user_about_repository.update(user_about, body)
        return self.response_updated('описание о вас обновлено')

    def delete(self, user_about_id: int) -> dict:
        user_about = self.user_about_repository.get_by_id(user_about_id)
        if not user_about or not user_about.user_id == g.user_id:
            return self.response_not_found('описание о вас не найдено')
        self.user_about_repository.delete(user_about)
        return self.response_deleted('описание о вас удалено')

    def get_by_id(self, user_about_id: int) -> dict:
        user_about = self.user_about_repository.get_by_id(user_about_id)
        if not user_about:
            return self.response_not_found('описание о вас не найдено')
        return self.response_ok(self.get_dict_items(user_about))

    def get_all(self, user_id: int) -> dict:
        user_abouts = self.user_about_repository.get_all(user_id)
        return self.response_ok(self.get_array_items(user_abouts))
