from src.__Parents.Service import Service
from .IUserImageRepo import IUserImageRepo
from src.User.IUserRepo import IUserRepo
from flask import g
import os
from src import app
from datetime import datetime


class UserImageService(Service):

    def __init__(self, user_image_repository: IUserImageRepo, user_repository: IUserRepo):
        self.user_image_repository: IUserImageRepo = user_image_repository
        self.user_repository: IUserRepo = user_repository

    def create(self, image) -> dict:
        filename = f"{g.user_id}{datetime.utcnow().strftime('%B:%d:%Y:%H:%M:%S')}{image.filename}"
        image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
        self.user_image_repository.create(filename=filename)
        self.user_repository.update(g.user_id, body={'image_path': filename})
        return self.response_created(msg_rus='фото успешно загружено',
                                     msg_eng='photo uploaded successfully',
                                     msg_arm='լուսանկարը հաջողությամբ վերբեռնվեց')

    def delete(self, filename: str) -> dict:
        user_image = self.user_image_repository.get_by_filename(filename)
        if not user_image or not user_image.user_id == g.user_id:
            return self.response_not_found(msg_rus='фото не найдено',
                                           msg_arm='լուսանկարը չի գտնվել',
                                           msg_eng='photo not found')

        self.user_image_repository.delete(user_image)
        os.remove(app.config["IMAGE_UPLOADS"] + '/' + filename)
        return self.response_deleted(msg_rus='фото пользователя удалено',
                                     msg_eng='photo removed',
                                     msg_arm='լուսանկարը հեռացվել է')

    def get_by_filename(self, filename: str) -> dict:
        return self.response_ok(self.get_encode_image(filename))
