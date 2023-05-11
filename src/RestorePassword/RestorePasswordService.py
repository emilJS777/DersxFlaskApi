from ..Email.IEmaiRepo import IEmailRepo
from ..Email.IEmailSender import IEmailSender
from ..__Parents.Repository import Repository
from .IRestorePasswordRepo import IRestorePasswordRepo
from ..__Parents.Service import Service
from src.Email.EmailHtml import EmailHtml


class RestorePasswordService(Service, Repository):
    def __init__(self, restore_password_repository: IRestorePasswordRepo, email_repository: IEmailRepo, email_sender: IEmailSender):
        self.restore_password_repository: IRestorePasswordRepo = restore_password_repository
        self.email_repository: IEmailRepo = email_repository
        self.email_sender: IEmailSender = email_sender

    def create(self, body: dict) -> dict:
        email = self.email_repository.get_by_address(address=body['address'])
        if not email:
            return self.response_not_found(msg_rus='адрес эл. почты не найден в системе',
                                           msg_arm='էլեկտրոնային  փոստը համակարգում չի գտնվել',
                                           msg_eng='Email not found in the system')
        random_code = self.generate_random_code()

        old_password_restore = self.restore_password_repository.get_by_user_id(user_id=email.user_id)
        if old_password_restore:
            self.restore_password_repository.update(restore_password=old_password_restore, security_code=random_code)
        else:
            self.restore_password_repository.create(user_id=email.user_id, security_code=random_code)

        self.email_sender.send(addresses=[email.address], header='password recovery', html=EmailHtml.password_restore(code=random_code))
        return self.response_created(msg_rus='на вашу эл. почту было отправлено письмо для обновления пароля',
                                     msg_eng='An email has been sent to your email address to reset your password',
                                     msg_arm='գաղտնաբառը վերականգնելու համար նամակ է ուղարկվել Ձեր էլ. հասցեին')

    def update(self, security_code: str, body: dict) -> dict:
        restore_password = self.restore_password_repository.get_by_security_code(security_code=security_code)
        if not restore_password:
            return self.response_not_found(msg_rus='код для восстановления пароля не верный',
                                           msg_arm='գաղտնաբառի վերականգնման կոդը ճիշտ չէ',
                                           msg_eng='password recovery code is not correct')
        self.restore_password_repository.restore_password(user=restore_password.user, new_password=body['new_password'])
        self.restore_password_repository.delete(restore_password=restore_password)
        return self.response_updated(msg_rus='пароль успешно изменен',
                                     msg_eng='password changed successfully',
                                     msg_arm='գաղտնաբառը հաջողությամբ փոխվել է')

    def get(self, security_code: str) -> dict:
        restore_password = self.restore_password_repository.get_by_security_code(security_code=security_code)
        if not restore_password:
            return self.response_not_found(msg_rus='код для восстановления пароля не верный',
                                           msg_arm='գաղտնաբառի վերականգնման կոդը ճիշտ չէ',
                                           msg_eng='password recovery code is not correct')
        return self.response_ok({'user': {
            'name': restore_password.user.name,
            'first_name': restore_password.user.first_name,
            'last_name': restore_password.user.last_name,
            'image': self.get_dict_items(restore_password.user.image) if restore_password.user.image else None,
        }})
        