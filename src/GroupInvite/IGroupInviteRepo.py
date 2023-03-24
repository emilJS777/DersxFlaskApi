from abc import ABC, abstractmethod
from .GroupInviteModel import GroupInvite


class IGroupInviteRepo(ABC):
    @abstractmethod
    def create(self, body: dict) -> GroupInvite:
        pass

    @abstractmethod
    def update(self, group_invite: GroupInvite):
        pass

    @abstractmethod
    def delete(self, group_invite: GroupInvite):
        pass

    @abstractmethod
    def get(self, group_invite_id: int = None, user_id: int = None, group_id: int = None) -> GroupInvite:
        pass
        