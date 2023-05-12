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

            if decode:
                auth = AuthMiddleware.__auth_repository.get_by_user_id(decode['user_id'])
                if auth:
                    g.user = auth.user
                    g.user_id = decode['user_id']
                    g.admin = auth.user.admin
                    return f(*args, **kwargs)
            return AuthMiddleware.response_invalid_login(msg_rus='Неверное имя пользователя и / или пароль',
                                                         msg_arm='անվավեր օգտանուն և/կամ գաղտնաբառ',
                                                         msg_eng='invalid username and/or password')

        return decorated_function

    @staticmethod
    def check_admin():
        def decoration(f):
            @wraps(f)
            def decoration_function(*args, **kwargs):
                if not g.admin:
                    return AuthMiddleware.response_invalid_login(msg_eng='forbidden resource',
                                                                 msg_rus='запрещенный ресурс',
                                                                 msg_arm='արգելված ռեսուրս')
                return f(*args, **kwargs)
            return decoration_function
        return decoration

