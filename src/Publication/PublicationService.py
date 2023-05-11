from src.Image.IImageRepo import IImageRepo
from .IPublicationRepo import IPublicationRepo
from ..__Parents.Repository import Repository
from ..__Parents.Service import Service


class PublicationService(Service, Repository):
    def __init__(self, publication_repository: IPublicationRepo, image_repository: IImageRepo):
        self.publication_repository: IPublicationRepo = publication_repository
        self.image_repository: IImageRepo = image_repository

    def create(self, body: dict) -> dict:
        publication = self.publication_repository.create(body)
        return self.response_created(msg_rus="публикация успешно создана",
                                     msg_eng="publication successfully created",
                                     msg_arm="հրապարակումը հաջողությամբ ստեղծվաց է",
                                     obj_id=publication.id)

    def update(self, publication_id: int, body: dict) -> dict:
        publication = self.publication_repository.get_by_id(publication_id)
        if not publication:
            return self.response_not_found(msg_rus='публикация не найдена',
                                           msg_arm='հրապարակումը չի գտնվել',
                                           msg_eng='publication not found')

        self.publication_repository.update(publication=publication, body=body)
        return self.response_updated(msg_rus='публикация успешно обновлена',
                                     msg_eng='publication successfully updated',
                                     msg_arm='հրապարակումը թարմացվել է')

    def delete(self, publication_id: int) -> dict:
        publication = self.publication_repository.get_by_id(publication_id)
        if not publication:
            return self.response_not_found(msg_rus='публикация не найдена',
                                           msg_arm='հրապարակումը չի գտնվել',
                                           msg_eng='publication not found')

        if publication.image:
            self.image_repository.delete(publication.image)

        self.publication_repository.delete(publication)
        return self.response_deleted(msg_rus='публикация успешно удалена',
                                     msg_eng='publication successfully deleted',
                                     msg_arm='հրապարակումը հաջողությամբ ջնջվել է')

    def get_by_id(self, publication_id: int) -> dict:
        publication = self.publication_repository.get_by_id(publication_id)
        if not publication:
            return self.response_not_found(msg_rus='публикация не найдена',
                                           msg_arm='հրապարակումը չի գտնվել',
                                           msg_eng='publication not found')
        return self.response_ok({
            'id': publication.id,
            'description': publication.description,
            'image': self.get_dict_items(publication.image) if publication.image else None,
            'creation_date': publication.creation_date,
            'creator': {
                'id': publication.creator.id,
                'first_name': publication.creator.first_name,
                'last_name': publication.creator.last_name,
                'name': publication.creator.name,
                'image': self.get_dict_items(publication.creator.image) if publication.creator.image else None
            }
        })

    def get_all(self, limit: int, offset: int, creator_id: int or None, liked_id: int or None) -> dict:
        publications: list = self.publication_repository.get_all(
            limit=limit,
            offset=offset,
            creator_id=creator_id,
            liked_id=liked_id)

        return self.response_ok([{
            'id': publication.id,
            'description': publication.description,
            'image': self.get_dict_items(publication.image) if publication.image else None,
            'creation_date': publication.creation_date,
            'comment_count': len(publication.comments),
            'like_count': len(publication.likes),
            'creator': {
                'id': publication.creator.id,
                'name': publication.creator.name,
                'first_name': publication.creator.first_name,
                'last_name': publication.creator.last_name,
                'image': self.get_dict_items(publication.creator.image) if publication.creator.image else None
            }
        } for publication in publications])
