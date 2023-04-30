from .IUserRepo import IUserRepo
from flask_bcrypt import check_password_hash
from flask import g

from ..Email.EmailHtml import EmailHtml
from ..Email.IEmaiRepo import IEmailRepo
from ..Email.IEmailSender import IEmailSender
from ..__Parents.Repository import Repository
from ..__Parents.Service import Service


class UserService(Service, Repository):
    def __init__(self, user_repository: IUserRepo, email_repository: IEmailRepo, email_sender: IEmailSender):
        self._user_repository: IUserRepo = user_repository
        self.email_repository: IEmailRepo = email_repository
        self.email_sender: IEmailSender = email_sender

    # CREATE
    def create(self, body: dict) -> dict:
        if self._user_repository.get_by_name(body['name']):
            return self.response_conflict('имя пользователя существует в системе')

        if self.email_repository.get_by_address(address=body['email_address']):
            return self.response_conflict('адрес эл. почты существует в системе')

        user = self._user_repository.create(body=body)
        self.email_repository.create(user_id=user.id, body=body)
        return self.response_created('пользователь создан')

    # UPDATE
    def update(self, user_id: int, body: dict) -> dict:
        if not self._user_repository.get_by_id(user_id):
            return self.response_not_found('пользователь не найден')

        if body.get('name') and self._user_repository.get_by_name_exclude_id(user_id, body['name']):
            return self.response_conflict('имя пользователя существует в системе')

        if body.get('email_address') and self.email_repository.get_by_address_exclude_user_id(user_id, body['email_address']):
            return self.response_conflict('адрес эл. почты существует в системе')

        if body.get('email_address'):
            self.email_repository.update(email=g.user.email, body=body)
            code = self.generate_random_code()
            self.email_repository.update_activation_code(code=code)
            self.email_sender.send(addresses=[body['email_address']], header='подтверждения эл. почты', html=EmailHtml.email_activation(code))

        self._user_repository.update(user_id, body)
        return self.response_updated('данные пользователя успешно обновлены')

    # DELETE
    def delete(self, user_id: int, body: dict):
        user = self._user_repository.get_by_id(user_id)

        if not user:
            return self.response_not_found('пользователь не найден')

        if not check_password_hash(user['password_hash'], body['password']):
            return self.response_invalid_password()

        self._user_repository.delete(user_id)
        return self.response_deleted('пользователь удален')

    # GET BY ID
    def get_by_id(self, user_id: int) -> dict:
        user = self._user_repository.get_by_id(user_id)
        if not user:
            return self.response_not_found('пользователь не найден')

        return self.response_ok({
            'id': user.id,
            'name': user.name,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': self.get_dict_items(user.email),
            'date_birth': user.date_birth,
            'region': user.region,
            'role_id': user.role_id,
            'image': self.get_dict_items(user.image) if user.image else None,
            'gender_id': user.gender_id,
            'gender': self.get_dict_items(user.gender),
            'creation_date': user.creation_date.strftime("%Y-%m-%d")
        })

    # GET ALL
    def get_all(self, page: int, per_page: int, rubric_id: int or None, role_id: int or None, category_ids: list[int] or None,
                search: int or None,  group_id: int or None, not_group_id: int or None) -> dict:
        users: dict = self._user_repository.get_all(
            page=page,
            per_page=per_page,
            rubric_id=rubric_id,
            role_id=role_id,
            category_ids=category_ids,
            search=search,
            group_id=group_id,
            not_group_id=not_group_id)
        return self.response_ok({
            'total': users.total,
            'page': users.page,
            'pages': users.pages,
            'per_page': users.per_page,
            'items': [{
                'id': user.id,
                'name': user.name,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': self.get_dict_items(user.email),
                'role_id': user.role_id,
                'gender': self.get_dict_items(user.gender),
                'image': self.get_dict_items(user.image) if user.image else None,
            } for user in users.items]
        })

