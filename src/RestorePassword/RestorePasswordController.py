from .RestorePasswordService import RestorePasswordService
from .RestorePasswordRepository import RestorePasswordRepository
from ..__Parents.Controller import Controller
from src.Email.EmailRepository import EmailRepository
from src.Email.EmailSender import EmailSender
from flask_expects_json import expects_json
from .RestoreRasswordValidator import create_restore_password_schema, update_restore_password_schema


class RestorePasswordController(Controller):
    restore_password_service: RestorePasswordService = RestorePasswordService(RestorePasswordRepository(), EmailRepository(), EmailSender())

    @expects_json(create_restore_password_schema)
    def post(self) -> dict:
        res: dict = self.restore_password_service.create(body=self.request.get_json())
        return res

    @expects_json(update_restore_password_schema)
    def put(self) -> dict:
        res: dict = self.restore_password_service.update(security_code=self.arguments.get('security_code'), body=self.request.get_json())
        return res

    def get(self) -> dict:
        res: dict = self.restore_password_service.get(security_code=self.arguments.get('security_code'))
        return res
        