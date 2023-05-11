from src.__Parents.Repository import Repository
from src.__Parents.Service import Service
from .IWorkExperienceRepo import IWorkExperienceRepo
from flask import g


class WorkExperienceService(Service, Repository):

    def __init__(self, work_experience_repository: IWorkExperienceRepo):
        self.work_experience_repository: IWorkExperienceRepo = work_experience_repository

    def create(self, body: dict) -> dict:
        self.work_experience_repository.create(body)
        return self.response_created(msg_rus='опыт работы было создано',
                                     msg_eng='work experience has been created',
                                     msg_arm='աշխատանքային փորձը ստեղծվել է')

    def update(self, work_experience_id: int, body: dict) -> dict:
        work_experience = self.work_experience_repository.get_by_id(work_experience_id=work_experience_id)
        if not work_experience or not work_experience.user_id == g.user_id:
            return self.response_not_found(msg_rus='опыт работы не найдено',
                                           msg_arm='աշխատանքային փորձը չի գտնվել',
                                           msg_eng='work experience not found')

        self.work_experience_repository.update(work_experience=work_experience, body=body)
        return self.response_updated(msg_rus='опыт работы было обновлено',
                                     msg_arm='աշխատանքային փորձը թարմացվել է',
                                     msg_eng='work experience updated')

    def delete(self, work_experience_id: int) -> dict:
        work_experience = self.work_experience_repository.get_by_id(work_experience_id=work_experience_id)
        if not work_experience or not work_experience.user_id == g.user_id:
            return self.response_not_found(msg_rus='опыт работы не найдено',
                                           msg_arm='աշխատանքային փորձը չի գտնվել',
                                           msg_eng='work experience not found')

        self.work_experience_repository.delete(work_experience)
        return self.response_deleted(msg_rus='опыт работы было удалено',
                                     msg_arm='աշխատանքային փորձը ջնջված է',
                                     msg_eng='work experience deleted')

    def get_by_id(self, work_experience_id: int) -> dict:
        work_experience = self.work_experience_repository.get_by_id(work_experience_id=work_experience_id)
        if not work_experience:
            return self.response_not_found(msg_rus='опыт работы не найдено',
                                           msg_arm='աշխատանքային փորձը չի գտնվել',
                                           msg_eng='work experience not found')

        return self.response_ok(self.get_dict_items(work_experience))

    def get_all(self, user_id: int) -> dict:
        work_experiences = self.work_experience_repository.get_all(user_id=user_id)
        return self.response_ok(self.get_array_items(work_experiences))
