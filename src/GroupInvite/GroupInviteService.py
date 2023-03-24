from ..Notification.INotificationRepo import INotificationRepo
from ..__Parents.Repository import Repository
from .IGroupInviteRepo import IGroupInviteRepo
from ..__Parents.Service import Service
from flask import g


class GroupInviteService(Service, Repository):
    def __init__(self, group_invite_repository: IGroupInviteRepo, notification_repository: INotificationRepo):
        self.group_invite_repository: IGroupInviteRepo = group_invite_repository
        self.notification_repository: INotificationRepo = notification_repository

    def create(self, body: dict) -> dict:
        group_invite = self.group_invite_repository.create(body=body)
        if not group_invite.group.creator_id == g.user_id:
            self.group_invite_repository.delete(group_invite)
            return self.response_deleted('группа не найдена')
        self.notification_repository.create(user_id=group_invite.user_id, group_invite_id=group_invite.id)
        return self.response_created()

    def update(self, group_invite_id: int) -> dict:
        group_invite = self.group_invite_repository.get(group_invite_id=group_invite_id)
        if not group_invite or not group_invite.user_id == g.user_id:
            return self.response_not_found('приглашение не найдено')
        self.notification_repository.delete(group_invite_id=group_invite.id)
        self.group_invite_repository.update(group_invite=group_invite)
        return self.response_updated()

    def delete(self, group_id: int, user_id: int) -> dict:
        group_invite = self.group_invite_repository.get(user_id=user_id, group_id=group_id)
        if not group_invite:
            return self.response_not_found('приглашение было найдено')
        self.notification_repository.delete(group_invite_id=group_invite.id)
        if group_invite.user_id == g.user_id:
            self.group_invite_repository.delete(group_invite)
            return self.response_deleted('приглашение отклонено')
        if group_invite.group.creator_id == g.user_id:
            self.group_invite_repository.delete(group_invite)
        return self.response_deleted('приглашение отменено')

    def get(self, group_id: int, user_id: int) -> dict:
        group_invite = self.group_invite_repository.get(group_id=group_id, user_id=user_id)
        if not group_invite:
            return self.response_not_found()
        return self.response_ok(self.get_dict_items(group_invite))
