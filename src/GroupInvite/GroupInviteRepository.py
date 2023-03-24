from .IGroupInviteRepo import IGroupInviteRepo
from .GroupInviteModel import GroupInvite


class GroupInviteRepository(IGroupInviteRepo):
    def create(self, body: dict) -> GroupInvite:
        groupinvite: GroupInvite = GroupInvite()
        groupinvite.user_id = body['user_id']
        groupinvite.group_id = body['group_id']
        groupinvite.confirmed = False
        groupinvite.save_db()
        return groupinvite

    def update(self, group_invite: GroupInvite):
        group_invite.confirmed = True
        group_invite.update_db()
        
    def delete(self, group_invite: GroupInvite):
        group_invite.delete_db()

    def get(self, group_invite_id: int = None, user_id: int = None, group_id: int = None) -> GroupInvite:
        group_invite: GroupInvite = GroupInvite.query.filter(
            GroupInvite.id == group_invite_id if group_invite_id else GroupInvite.id.isnot(None),
            GroupInvite.group_id == group_id if group_id else GroupInvite.id.isnot(None),
            GroupInvite.user_id == user_id if user_id else GroupInvite.id.isnot(None)
        ).first()
        return group_invite
        