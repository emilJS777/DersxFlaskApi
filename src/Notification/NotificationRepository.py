from .INotificationRepo import INotificationRepo
from .NotificationModel import Notification
from flask import g

from ..Socketio.ISocketio import ISocketio


class NotificationRepository(INotificationRepo):
    def __init__(self, socket_io: ISocketio):
        self.socket_io: ISocketio = socket_io

    def create(self, user_id: int, friend_id: int = None, vacancy_offer_id: int = None, team_id: int = None) -> Notification:
        notification: Notification = Notification()
        notification.creator_id = g.user_id
        notification.user_id = user_id

        notification.friend_id = friend_id
        notification.vacancy_offer_id = vacancy_offer_id
        notification.team_id = team_id

        notification.save_db()

        self.socket_io.send(
            emit_name="notification_ids",
            data={"notification_ids": [notification.id]},
            user_id=user_id)

        return notification

    def delete(self, notification: Notification = None, friend_id: int = None):
        if notification:
            notification.delete_db()
        if friend_id:
            Notification.query.filter_by(friend_id=friend_id).delete()

    def get_by_id(self, notification_id: int = None) -> Notification:
        return Notification.query.filter_by(user_id=g.user_id, id=notification_id).first()

    def get_all(self) -> list[Notification]:
        notifications = Notification.query.filter(Notification.user_id == g.user_id).all()
        return notifications
