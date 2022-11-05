from .IPublicationLikeRepo import IPublicationLikeRepo
from ..__Parents.Service import Service
from flask import g


class PublicationLikeService(Service):

    def __init__(self, publication_like_repository: IPublicationLikeRepo):
        self.publication_like_repository: IPublicationLikeRepo = publication_like_repository

    def create(self, body: dict) -> dict:
        self.publication_like_repository.create(body)
        return self.response_created('лайк для публикации создано')

    def delete(self, publication_id: int) -> dict:
        publication_like = self.publication_like_repository.get(publication_id=publication_id, user_id=g.user_id)
        if not publication_like:
            return self.response_not_found('лайк для публикации не найдено')
        self.publication_like_repository.delete(publication_like)
        return self.response_deleted('лайк для публикации удалено')

    def get(self, publication_id: int) -> dict:
        publication_like = self.publication_like_repository.get(publication_id=publication_id, user_id=g.user_id)
        if not publication_like:
            return self.response_not_found()
        return self.response_ok({'like': True})
