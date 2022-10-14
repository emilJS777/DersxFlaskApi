from functools import wraps
from flask import g, request
from flask_jwt_extended import jwt_required, get_jwt_identity, verify_jwt_in_request
import jwt
from src.Auth.AuthRepository import AuthRepository
from src.Auth.IAuthRepo import IAuthRepo
from src.User.UserRepository import UserRepository
from src.User.IUserRepo import IUserRepo
from src.__Parents.Service import Service
from src import app


class AuthMiddleware(Service):
    __auth_repository: IAuthRepo = AuthRepository()
    __user_repository: IUserRepo = UserRepository()

    @staticmethod
    def check_authorize(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            decode = jwt.decode(request.headers['Authorization'].split(' ')[1],
                                app.config['JWT_SECRET_KEY'],
                                algorithms=[app.config['JWT_ALGORITHM']])

            if decode and AuthMiddleware.__auth_repository.get_by_user_id(decode['user_id']):
                g.user_id = decode['user_id']
                return f(*args, **kwargs)
            return AuthMiddleware.response_invalid_login()

        return decorated_function

    # @staticmethod
    # def check_authorize(f):
    #     @wraps(f)
    #     @jwt_required()
    #     def decorated_function(*args, **kwargs):
    #
    #         auth = AuthMiddleware.__auth_repository.get_by_user_id(user_id=get_jwt_identity())
    #         if auth['access_token'] == request.headers['authorization'].split(' ')[1]:
    #
    #             if AuthMiddleware.__user_repository.get_by_id(auth['user_id']):
    #                 g.user_id = get_jwt_identity()
    #                 return f(*args, **kwargs)
    #
    #         return Service.response_invalid_login()
    #     return decorated_function

