from .IAuthRepo import IAuthRepo
from src.User.IUserRepo import IUserRepo
from flask_bcrypt import check_password_hash

from ..__Parents.Repository import Repository
from ..__Parents.Service import Service
from flask_jwt_extended import get_jwt_identity
from flask import request, g


class AuthService(Service, Repository):
    def __init__(self, auth_repository: IAuthRepo, user_repository: IUserRepo):
        self.__auth_repository = auth_repository
        self.__user_repository = user_repository

    def login(self, body: dict) -> dict:
        user = self.__user_repository.get_by_name_or_email(body['name'])

        if not user or not check_password_hash(user.password_hash, body['password']):
            return self.response_invalid_login(msg_rus='Неверное имя пользователя и / или пароль',
                                               msg_arm='անվավեր օգտանուն և/կամ գաղտնաբառ',
                                               msg_eng='invalid username and/or password')

        auth = self.__auth_repository.generate_tokens(user.id)
        return self.response_ok(auth)

    def logout(self) -> dict:
        self.__auth_repository.delete_by_user_id(g.user_id)
        return self.response_deleted(msg_rus='', msg_eng='', msg_arm='')

    def refresh(self) -> dict:
        auth = self.__auth_repository.get_by_user_id(user_id=get_jwt_identity())
        if auth['refresh_token'] == request.headers['authorization'].split(' ')[1]:

            auth = self.__auth_repository.generate_tokens(get_jwt_identity())
            self.response_ok(auth)

        return self.response_invalid_login(msg_rus='Неверное имя пользователя и / или пароль',
                                           msg_arm='անվավեր օգտանուն և/կամ գաղտնաբառ',
                                           msg_eng='invalid username and/or password')

    def get_profile(self) -> dict:
        return self.response_ok({
            'id': g.user.id,
            'name': g.user.name,
            'admin': g.user.admin,
            'first_name': g.user.first_name,
            'last_name': g.user.last_name,
            'region': g.user.region,
            'email': self.get_dict_items(g.user.email),
            'date_birth': g.user.date_birth,
            'role_id': g.user.role_id,
            'image': self.get_encode_image(g.user.image.filename) if g.user.image else None,
            'gender_id': g.user.gender_id,
            'gender': self.get_dict_items(g.user.gender)
        })
