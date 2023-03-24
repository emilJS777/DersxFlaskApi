from operator import or_

from .IGroupRepo import IGroupRepo
from .GroupModel import Group
from flask import g


class GroupRepository(IGroupRepo):
    def create(self, body: dict) -> Group:
        group: Group = Group()
        group.title = body['title']
        group.description = body['description']
        group.creator_id = g.user_id
        group.users = [g.user]
        group.save_db()
        return group

    def update(self, group: Group, body: dict):
        group.title = body['title']
        group.description = body['description']
        group.update_db()
        
    def delete(self, group: Group):
        group.delete_db()

    def get_by_id(self, group_id: int) -> Group:
        group: Group = Group.query.filter_by(id=group_id).first()
        return group

    def get_all(self, page: int, per_page: int, search: str):
        groups: list[Group] = Group.query.filter(
            or_(Group.title.like(f'%{search}%'), Group.description.like(f'%{search}%')) if search else Group.id.isnot(None)
        ).paginate(page=page, per_page=per_page)
        return groups
        