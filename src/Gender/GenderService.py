from .IGenderRepo import IGenderRepo
from ..__Parents.Repository import Repository
from ..__Parents.Service import Service


class GenderService(Service, Repository):
    def __init__(self, gender_repository: IGenderRepo):
        self.gender_repository: IGenderRepo = gender_repository

    def create(self, body: dict) -> dict:
        self.gender_repository.create(body)
        return self.response_created(msg_rus='', msg_eng='', msg_arm='')

    def update(self, gender_id: int, body: dict) -> dict:
        gender = self.gender_repository.get_by_id(gender_id)
        if not gender:
            return self.response_not_found(msg_rus='', msg_eng='', msg_arm='')
        self.gender_repository.update(gender=gender, body=body)
        return self.response_updated(msg_rus='', msg_eng='', msg_arm='')

    def delete(self, gender_id: int) -> dict:
        gender = self.gender_repository.get_by_id(gender_id)
        if not gender:
            return self.response_not_found(msg_rus='', msg_eng='', msg_arm='')
        self.gender_repository.delete(gender)
        return self.response_deleted(msg_rus='', msg_eng='', msg_arm='')

    def get_by_id(self, gender_id: int) -> dict:
        gender = self.gender_repository.get_by_id(gender_id)
        if not gender:
            return self.response_not_found(msg_rus='', msg_eng='', msg_arm='')
        return self.response_ok(self.get_dict_items(gender))

    def get_all(self) -> dict:
        genders = self.gender_repository.get_all()
        return self.response_ok(self.get_array_items(genders))
