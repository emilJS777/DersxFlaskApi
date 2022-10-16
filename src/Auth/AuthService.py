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
        user = self.__user_repository.get_by_name(body['name'])

        if not user or not check_password_hash(user.password_hash, body['password']):
            return self.response_invalid_login()

        auth = self.__auth_repository.generate_tokens(user.id)
        return self.response_ok(auth)

    def logout(self) -> dict:
        self.__auth_repository.delete_by_user_id(g.user_id)
        return self.response_deleted('выход из аккаунта прошла успешно')

    def refresh(self) -> dict:
        auth = self.__auth_repository.get_by_user_id(user_id=get_jwt_identity())
        if auth['refresh_token'] == request.headers['authorization'].split(' ')[1]:

            auth = self.__auth_repository.generate_tokens(get_jwt_identity())
            self.response_ok(auth)

        return self.response_invalid_login()

    def get_profile(self) -> dict:
        profile = self.__user_repository.get_by_id(g.user_id)
        return self.response_ok({
            'id': profile.id,
            'name': profile.name,
            'first_name': profile.first_name,
            'last_name': profile.last_name,
            'email_address': profile.email_address,
            'date_birth': profile.date_birth,
            'role_id': profile.role_id,
            'image': self.get_encode_image(profile.image.filename) if profile.image else None,
            'gender_id': profile.gender_id,
            'gender': self.get_dict_items(profile.gender)
        })
