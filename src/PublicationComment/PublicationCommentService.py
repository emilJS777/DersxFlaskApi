from .IPublicationCommentRepo import IPublicationCommentRepo
from ..Notification.INotificationRepo import INotificationRepo
from ..__Parents.Service import Service
from flask import g


class PublicationCommentService(Service):

    def __init__(self, publication_comment_repository: IPublicationCommentRepo, notification_repository: INotificationRepo):
        self.publication_comment_repository: IPublicationCommentRepo = publication_comment_repository
        self.notification_repository: INotificationRepo = notification_repository

    def create(self, body: dict) -> dict:
        publication_comment = self.publication_comment_repository.create(body)
        self.notification_repository.create(publication_comment_id=publication_comment.id, user_id=publication_comment.publication.creator_id)
        return self.response_created(msg_arm='комментария успешно создано',
                                     msg_eng='comment successfully created',
                                     msg_rus='մեկնաբանությունը հաջողությամբ ստեղծվեց')

    def update(self, publication_comment_id: int, body: dict) -> dict:
        publication_comment = self.publication_comment_repository.get_by_id(publication_comment_id)
        if not publication_comment or not publication_comment.creator_id == g.user_id:
            return self.response_not_found(msg_rus='комментария не найдено',
                                           msg_eng='comment not found',
                                           msg_arm='մեկնաբանությունը չի գտնվել')
        self.publication_comment_repository.update(
            publication_comment=publication_comment,
            body=body)
        return self.response_updated(msg_rus='комментария успешно обновлено',
                                     msg_eng='comment successfully updated',
                                     msg_arm='մեկնաբանությունը հաջողությամբ թարմացվել է')

    def delete(self, publication_comment_id: int) -> dict:
        publication_comment = self.publication_comment_repository.get_by_id(publication_comment_id)
        if not publication_comment or not publication_comment.creator_id == g.user_id:
            return self.response_not_found(msg_rus='комментария не найдено',
                                           msg_eng='comment not found',
                                           msg_arm='մեկնաբանությունը չի գտնվել')
        self.publication_comment_repository.delete(publication_comment)
        return self.response_deleted(msg_rus='комментария успешно удалено',
                                     msg_arm='մեկնաբանությունը հաջողությամբ ջնջվել է',
                                     msg_eng='comment successfully deleted')

    def get_by_id(self, publication_comment_id: int) -> dict:
        publication_comment = self.publication_comment_repository.get_by_id(publication_comment_id)
        if not publication_comment:
            return self.response_not_found(msg_rus='комментария не найдено',
                                           msg_eng='comment not found',
                                           msg_arm='մեկնաբանությունը չի գտնվել')
        return self.response_ok({
            'id': publication_comment.id,
            'text': publication_comment.text})

    def get_all(self, limit: int, offset: int, publication_id: int) -> dict:
        publication_comments: list = self.publication_comment_repository.get_all(
            limit=limit,
            offset=offset,
            publication_id=publication_id)
        return self.response_ok([{
            'id': publication_comment.id,
            'text': publication_comment.text,
            'creation_date': publication_comment.creation_date,
            'creator': {
                'id': publication_comment.creator.id,
                'name': publication_comment.creator.name,
                'first_name': publication_comment.creator.first_name,
                'last_name': publication_comment.creator.last_name,
                'image': self.get_encode_image(publication_comment.creator.image.filename) if publication_comment.creator.image else None
            }
        } for publication_comment in publication_comments])

