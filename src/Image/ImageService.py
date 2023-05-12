from src import app
from .IImageRepo import IImageRepo
from ..__Parents.Service import Service
from flask import g
from flask import send_file


class ImageService(Service):
    def __init__(self, image_repository: IImageRepo):
        self.image_repository: IImageRepo = image_repository

    def create(self, image, user_id: int or None, service_id: int or None, publication_id: int or None, company_id: int or None, group_id: int or None) -> dict:
        self.image_repository.create(
            image=image,
            user_id=user_id,
            service_id=service_id,
            publication_id=publication_id,
            company_id=company_id,
            group_id=group_id)

        return self.response_created(msg_rus='данные загружены',
                                     msg_arm='տվյալները բեռնված են',
                                     msg_eng='data loaded')

    def delete(self, filename: str = None) -> dict:
        image = self.image_repository.get(filename=filename)
        if not image or not image.creator_id == g.user_id:
            return self.response_not_found(msg_rus='изображение не найдено',
                                           msg_eng='image not found',
                                           msg_arm='պատկերը չի գտնվել')

        self.image_repository.delete(image)
        return self.response_deleted(msg_rus='изображение удалено',
                                     msg_eng='image removed',
                                     msg_arm='պատկերը հեռացված է')

    def get(self, filename: str):
        return send_file('../'+app.config["IMAGE_UPLOADS"]+'/'+filename,
                         mimetype=None,
                         as_attachment=False,
                         conditional=False)
        # return send_file(app.config["IMAGE_UPLOADS"]+'/'+filename, mimetype="image/jpeg")
