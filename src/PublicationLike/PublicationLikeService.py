from .IPublicationLikeRepo import IPublicationLikeRepo
from ..__Parents.Service import Service
from flask import g


class PublicationLikeService(Service):

    def __init__(self, publication_like_repository: IPublicationLikeRepo):
        self.publication_like_repository: IPublicationLikeRepo = publication_like_repository

    def create(self, body: dict) -> dict:
        self.publication_like_repository.create(body)
        return self.response_created(msg_rus='', msg_arm='', msg_eng='')

    def delete(self, publication_id: int) -> dict:
        publication_like = self.publication_like_repository.get(publication_id=publication_id, user_id=g.user_id)
        if not publication_like:
            return self.response_not_found(msg_rus='', msg_arm='', msg_eng='')
        self.publication_like_repository.delete(publication_like)
        return self.response_deleted(msg_rus='', msg_arm='', msg_eng='')

    def get(self, publication_id: int) -> dict:
        publication_like = self.publication_like_repository.get(publication_id=publication_id, user_id=g.user_id)
        if not publication_like:
            return self.response_not_found(msg_eng='', msg_arm='', msg_rus='')
        return self.response_ok({'like': True})
