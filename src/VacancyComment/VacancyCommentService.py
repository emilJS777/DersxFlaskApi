from .IVacancyCommentRepo import IVacancyCommentRepo
from ..__Parents.Repository import Repository
from ..__Parents.Service import Service
from flask import g


class VacancyCommentService(Service, Repository):

    def __init__(self, vacancy_comment_repository: IVacancyCommentRepo):
        self.vacancy_comment_repository: IVacancyCommentRepo = vacancy_comment_repository

    def create(self, body: dict) -> dict:
        self.vacancy_comment_repository.create(body)
        return self.response_created(msg_rus='комментарий был успешно создан',
                                     msg_eng='comment was created successfully',
                                     msg_arm='մեկնաբանությունը հաջողությամբ ստեղծվեց')

    def update(self, vacancy_comment_id: int, body: dict) -> dict:
        print(body)
        vacancy_comment = self.vacancy_comment_repository.get_by_id(vacancy_comment_id)
        if not vacancy_comment or not vacancy_comment.user_id == g.user_id:
            return self.response_not_found(msg_rus='комментарий не был найден',
                                           msg_arm='մեկնաբանությունը չի գտնվել',
                                           msg_eng='comment was not found')

        self.vacancy_comment_repository.update(vacancy_comment=vacancy_comment, body=body)
        return self.response_updated(msg_rus='комментарий успешно обновлен',
                                     msg_eng='comment successfully updated',
                                     msg_arm='մեկնաբանությունը հաջողությամբ թարմացվեց')

    def delete(self, vacancy_comment_id: int) -> dict:
        vacancy_comment = self.vacancy_comment_repository.get_by_id(vacancy_comment_id)
        if not vacancy_comment or not vacancy_comment.user_id == g.user_id:
            return self.response_not_found(msg_rus='комментарий не был найден',
                                           msg_arm='մեկնաբանությունը չի գտնվել',
                                           msg_eng='comment was not found')
        self.vacancy_comment_repository.delete(vacancy_comment)
        return self.response_deleted(msg_rus='комментарий успешно удален',
                                     msg_eng='comment successfully deleted',
                                     msg_arm='մեկնաբանությունը հաջողությամբ ջնջվեց')

    def get_by_id(self, vacancy_comment_id: int) -> dict:
        vacancy_comment = self.vacancy_comment_repository.get_by_id(vacancy_comment_id)
        if not vacancy_comment:
            return self.response_not_found(msg_rus='комментарий не был найден',
                                           msg_arm='մեկնաբանությունը չի գտնվել',
                                           msg_eng='comment was not found')
        return self.response_ok(self.get_dict_items(vacancy_comment))

    def get_all(self, page: int, per_page: int, vacancy_id: int) -> dict:
        vacancy_comments = self.vacancy_comment_repository.get_all(page=page, per_page=per_page, vacancy_id=vacancy_id)
        return self.response_ok({
            'total': vacancy_comments.total,
            'page': vacancy_comments.page,
            'pages': vacancy_comments.pages,
            'per_page': vacancy_comments.per_page,
            'items': [{
                'id': vacancy_comment.id,
                'text': vacancy_comment.text,
                'user': {
                    'id': vacancy_comment.user.id,
                    'name': vacancy_comment.user.name,
                    'first_name': vacancy_comment.user.first_name,
                    'last_name': vacancy_comment.user.last_name,
                    'image': self.get_dict_items(vacancy_comment.user.image) if vacancy_comment.user.image else None
                },
                'creation_date': vacancy_comment.creation_date
            } for vacancy_comment in vacancy_comments.items]
        })
