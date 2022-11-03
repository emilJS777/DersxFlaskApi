import os
from src.PublicationImage.IPublicationImageRepo import IPublicationImageRepo
from .IPublicationRepo import IPublicationRepo
from ..__Parents.Service import Service
from src import app


class PublicationService(Service):
    def __init__(self, publication_repository: IPublicationRepo, publication_image_repository: IPublicationImageRepo):
        self.publication_repository: IPublicationRepo = publication_repository
        self.publication_image_repository: IPublicationImageRepo = publication_image_repository

    def create(self, body: dict) -> dict:
        publication = self.publication_repository.create(body)
        return self.response_ok({"id": publication.id, "msg": "публикация успешно создана"})

    def update(self, publication_id: int, body: dict) -> dict:
        publication = self.publication_repository.get_by_id(publication_id)
        if not publication:
            return self.response_not_found('публикация не найдена')

        self.publication_repository.update(publication=publication, body=body)
        return self.response_updated('публикация успешно обновлена')

    def delete(self, publication_id: int) -> dict:
        publication = self.publication_repository.get_by_id(publication_id)
        if not publication:
            return self.response_not_found('публикация не найдена')

        if publication.image:
            os.remove(app.config["PUBLICATION_IMAGE_UPLOADS"] + '/' + publication.image.filename)
            self.publication_image_repository.delete(publication_image=publication.image)
        self.publication_repository.delete(publication)
        return self.response_deleted('публикация успешно удалена')

    def get_by_id(self, publication_id: int) -> dict:
        publication = self.publication_repository.get_by_id(publication_id)
        if not publication:
            return self.response_not_found('публикация не найдена')
        return self.response_ok({
            'id': publication.id,
            'description': publication.description,
            'image': self.get_encode_image(image_path=publication.image.filename, dir_path=app.config["PUBLICATION_IMAGE_UPLOADS"]) if publication.image else None,
            'creation_date': publication.creation_date,
            'creator': {
                'id': publication.creator.id,
                'first_name': publication.creator.first_name,
                'last_name': publication.creator.last_name,
                'name': publication.creator.name,
                'image': self.get_encode_image(publication.creator.image.filename) if publication.creator.image else None,
            }
        })

    def get_all(self, limit: int, offset: int, creator_id: int or None) -> dict:
        publications: list = self.publication_repository.get_all(
            limit=limit,
            offset=offset,
            creator_id=creator_id)

        return self.response_ok([{
            'id': publication.id,
            'description': publication.description,
            'image': self.get_encode_image(image_path=publication.image.filename, dir_path=app.config["PUBLICATION_IMAGE_UPLOADS"]) if publication.image else None,
            'creation_date': publication.creation_date,
            'creator': {
                'id': publication.creator.id,
                'name': publication.creator.name,
                'first_name': publication.creator.first_name,
                'last_name': publication.creator.last_name,
                'image': self.get_encode_image(publication.creator.image.filename) if publication.creator.image else None,
            }
        } for publication in publications])
