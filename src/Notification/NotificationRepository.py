from .INotificationRepo import INotificationRepo
from .NotificationModel import Notification
from flask import g

from ..Socketio.ISocketio import ISocketio


class NotificationRepository(INotificationRepo):
    def __init__(self, socket_io: ISocketio):
        self.socket_io: ISocketio = socket_io

    def create(self, user_id: int, friend_id: int = None, vacancy_offer_id: int = None, group_invite_id: int = None, publication_comment_id: int = None) -> Notification:
        notification: Notification = Notification()
        notification.creator_id = g.user_id
        notification.user_id = user_id

        notification.friend_id = friend_id
        notification.vacancy_offer_id = vacancy_offer_id
        notification.group_invite_id = group_invite_id
        notification.publication_comment = publication_comment_id
        notification.save_db()

        self.socket_io.send(
            emit_name="notification_ids",
            data={"notification_ids": [notification.id]},
            user_id=user_id)

        return notification

    def delete(self, notification: Notification = None, friend_id: int = None, group_invite_id: int = None):
        try:
            if notification:
                notification.delete_db()
            else:
                notification: Notification = Notification.query.filter(
                    Notification.friend_id == friend_id if friend_id else Notification.id.isnot(None),
                    Notification.group_invite_id == group_invite_id if group_invite_id else Notification.id.isnot(
                        None)).first()
                notification.delete_db()
            self.socket_io.send(
                emit_name="delete_notification_id",
                data={"notification_id": notification.id},
                user_id=notification.user_id)
        except:
            return True

    def get_by_id(self, notification_id: int = None) -> Notification:
        return Notification.query.filter_by(user_id=g.user_id, id=notification_id).first()

    def get_all(self) -> list[Notification]:
        notifications = Notification.query.filter(Notification.user_id == g.user_id).all()
        return notifications
