from src.__Parents.Service import Service
from .IPublicationImageRepo import IPublicationImageRepo
from src.Publication.IPublicationRepo import IPublicationRepo
from flask import g
from datetime import datetime
from src import app
import os


class PublicationImageService(Service):
    def __init__(self, publication_image_repository: IPublicationImageRepo, publication_repository: IPublicationRepo):
        self.publication_image_repository: IPublicationImageRepo = publication_image_repository
        self.publication_repository: IPublicationRepo = publication_repository

    def create(self, publication_id: int, image) -> dict:
        publication = self.publication_repository.get_by_id(publication_id)
        if not publication or not  publication.creator_id == g.user_id:
            return self.response_not_found(msg_rus='публикация  не найдена',
                                           msg_arm='հրապարակումը չի գտնվել',
                                           msg_eng='publication not found')

        filename = f"{g.user_id}{datetime.utcnow().strftime('%B:%d:%Y:%H:%M:%S')}{image.filename}"
        image.save(os.path.join(app.config["PUBLICATION_IMAGE_UPLOADS"], filename))
        self.publication_image_repository.create(filename=filename, publication_id=publication_id)
        return self.response_created(msg_rus='данные публикации  успешно загружены',
                                     msg_eng='publication data successfully created',
                                     msg_arm='հրապարակման տվյալները հաջողությամբ բեռնված են')

    def delete(self, publication_id: int) -> dict:
        publication = self.publication_repository.get_by_id(publication_id)
        if not publication or not publication.creator_id == g.user_id:
            return self.response_not_found(msg_rus='публикация не найдена',
                                           msg_arm='հրապարակումը չի գտնվել',
                                           msg_eng='publication not found')

        os.remove(app.config["PUBLICATION_IMAGE_UPLOADS"] + '/' + publication.image.filename)
        self.publication_image_repository.delete(publication_image=publication.image)
        return self.response_deleted(msg_rus='картинка успешно удалена',
                                     msg_eng='image successfully deleted',
                                     msg_arm='նկարը հաջողությամբ ջնջվեց')

    def get(self, filename: str) -> dict:
        pass
