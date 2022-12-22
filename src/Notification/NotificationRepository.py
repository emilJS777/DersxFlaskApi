from .INotificationRepo import INotificationRepo
from .NotificationModel import Notification
from flask import g


class NotificationRepository(INotificationRepo):
    def create(self, user_id: int, friend_id: int = None, vacancy_offer_id: int = None) -> Notification:
        notification: Notification = Notification()
        notification.creator_id = g.user_id
        notification.user_id = user_id

        if friend_id:
            notification.friend_id = friend_id

        if vacancy_offer_id:
            notification.vacancy_offer_id = vacancy_offer_id

        notification.save_db()
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
