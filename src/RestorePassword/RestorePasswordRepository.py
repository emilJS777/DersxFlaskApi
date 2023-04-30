from .IRestorePasswordRepo import IRestorePasswordRepo
from .RestorePasswordModel import RestorePassword
from flask_bcrypt import generate_password_hash

from ..User.UserModel import User


class RestorePasswordRepository(IRestorePasswordRepo):
    def create(self, user_id: int, security_code: str):
        restore_password: RestorePassword = RestorePassword()
        restore_password.user_id = user_id
        restore_password.security_code = security_code
        restore_password.save_db()

    def update(self, restore_password: RestorePassword, security_code: str):
        restore_password.security_code = security_code
        restore_password.update_db()

    def restore_password(self, user: User, new_password: str):
        user.password_hash = generate_password_hash(new_password)
        user.update_db()
        
    def delete(self, restore_password: RestorePassword):
        restore_password.delete_db()

    def get_by_user_id(self, user_id: int):
        restore_password: RestorePassword = RestorePassword.query.filter_by(user_id=user_id).first()
        return restore_password

    def get_by_security_code(self, security_code: str) -> RestorePassword:
        restore_password: RestorePassword = RestorePassword.query.filter_by(security_code=security_code).first()
        return restore_password

    def get_all(self) -> list[RestorePassword]:
        restore_passwords: list[RestorePassword] = RestorePassword.query.filter_by().all()
        return restore_passwords
        