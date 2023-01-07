from .NotificationModel import Notification
from abc import ABC, abstractmethod


class INotificationRepo(ABC):

    @abstractmethod
    def create(self, user_id: int, friend_id: int = None, vacancy_offer_id: int = None, team_id: int = None) -> Notification:
        pass

    @abstractmethod
    def delete(self, notification: Notification = None, friend_id: int = None):
        pass

    @abstractmethod
    def get_by_id(self, notification_id) -> Notification:
        pass

    @abstractmethod
    def get_all(self) -> list[Notification]:
        pass


