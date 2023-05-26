from src.Notification.INotificationRepo import INotificationRepo
from src.Socketio.ISocketio import ISocketio
from src.__Parents.Repository import Repository
from src.__Parents.Service import Service
from flask import g


class NotificationService(Service, Repository):
    def __init__(self, notification_repository: INotificationRepo, socketio: ISocketio):
        self.notification_repository: INotificationRepo = notification_repository
        self.socketio: ISocketio = socketio

    def delete(self, notification_id: int) -> dict:
        notification = self.notification_repository.get_by_id(notification_id)
        if not notification:
            return self.response_not_found(msg_rus='уведомления не найдено',
                                           msg_arm='ծանուցումը չի գտնվել',
                                           msg_eng='notice not found')
        self.notification_repository.delete(notification)
        return self.response_deleted(msg_eng='', msg_rus='', msg_arm='')

    def get_by_id(self, notification_id: int) -> dict:
        notification = self.notification_repository.get_by_id(notification_id)
        return self.response_ok({
            'id': notification.id,
            'friend_id': notification.friend_id,
            'vacancy_offer_id': notification.vacancy_offer_id,
            'vacancy_offer': self.get_dict_items(notification.vacancy_offer) if notification.vacancy_offer_id else None,
            'friend': self.get_dict_items(notification.friend) if notification.friend else None,
            'publication_comment': self.get_dict_items(notification.publication_comment) if notification.publication_comment else None,
            'group_invite': {
                'id': notification.group_invite.id,
                'group': self.get_dict_items(notification.group_invite.group)
            } if notification.group_invite else None,
            "creator": {
                        'id': notification.creator.id,
                        'name': notification.creator.name,
                        'first_name': notification.creator.first_name,
                        'last_name': notification.creator.last_name,
                        # 'email': self.get_dict_items(notification.creator.email),
                        'role_id': notification.creator.role_id,
                        'gender': self.get_dict_items(notification.creator.gender),
                        'image': self.get_dict_items(notification.creator.image) if notification.creator.image else None
                    },
        })

    def get_all(self):
        notifications = self.notification_repository.get_all()
        data = {"notification_ids": [notification.id for notification in notifications]}
        self.socketio.send(
            emit_name="notification_ids",
            data=data,
            user_id=g.user_id)
        return self.response_ok({})
