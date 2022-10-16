import ast
from src.__Parents.Controller import Controller
from .UserService import UserService
from .UserRepository import UserRepository
from flask import g
from flask_expects_json import expects_json
from .UserValidator import user_create_schema, user_update_schema
from src.Auth.AuthMiddleware import AuthMiddleware


class UserController(Controller):
    user_service = UserService(UserRepository())

    @expects_json(user_create_schema)
    def post(self):
        return self.user_service.create(
            body=self.request.get_json()
        )

    @expects_json(user_update_schema)
    @AuthMiddleware.check_authorize
    def put(self):
        return self.user_service.update(
            user_id=g.user_id,
            body=self.request.get_json()
        )

    @AuthMiddleware.check_authorize
    def delete(self):
        return self.user_service.delete(
            user_id=g.user_id,
            body=self.request.get_json()
        )

    def get(self):
        if self.id:
            return self.user_service.get_by_id(self.id)

        else:
            return self.user_service.get_all(
                page=self.page,
                per_page=self.per_page,
                rubric_id=int(self.arguments.get("rubric_id") or 0),
                role_id=int(self.arguments.get('role_id') or 0),
                category_ids=ast.literal_eval(self.arguments.get('category_ids')),
                search=self.arguments.get('search') or None
            )
