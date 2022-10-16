from .IUserRepo import IUserRepo
from flask_bcrypt import check_password_hash
from ..__Parents.Repository import Repository
from ..__Parents.Service import Service


class UserService(Service, Repository):
    def __init__(self, user_repository: IUserRepo):
        self._user_repository: IUserRepo = user_repository

    # CREATE
    def create(self, body: dict) -> dict:
        if self._user_repository.get_by_name(body['name']):
            return self.response_conflict('имя пользователя существует в системе')

        user = self._user_repository.create(body=body)
        return self.response_created('пользователь создан')

    # UPDATE
    def update(self, user_id: int, body: dict) -> dict:
        if not self._user_repository.get_by_id(user_id):
            return self.response_not_found('пользователь не найден')

        if body.get('name') and self._user_repository.get_by_name_exclude_id(user_id, body['name']):
            return self.response_conflict('имя пользователя существует в системе')

        if body.get('email_address') and self._user_repository.get_by_email_address_exclude_id(user_id, body['email_address']):
            return self.response_conflict('электронная почта существует в системе')

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
            'email_address': user.email_address,
            'date_birth': user.date_birth,
            'role_id': user.role_id,
            'image': self.get_encode_image(user.image.filename) if user.image else None,
            'gender_id': user.gender_id,
            'gender': self.get_dict_items(user.gender)
        })

    # GET ALL
    def get_all(self, page: int, per_page: int, rubric_id: int, role_id: int or None, category_ids: list[int], search: int or None) -> dict:
        users: dict = self._user_repository.get_all(
            page=page,
            per_page=per_page,
            rubric_id=rubric_id,
            role_id=role_id,
            category_ids=category_ids,
            search=search)
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
                'email_address': user.email_address,
                'role_id': user.role_id,
                'gender': self.get_dict_items(user.gender),
                'image': self.get_encode_image(user.image.filename) if user.image else None,
            } for user in users.items]
        })

