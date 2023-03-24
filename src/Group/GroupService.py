from ..__Parents.Repository import Repository
from .IGroupRepo import IGroupRepo
from ..__Parents.Service import Service
from flask import g


class GroupService(Service, Repository):
    def __init__(self, group_repository: IGroupRepo):
        self.group_repository: IGroupRepo = group_repository

    def create(self, body: dict) -> dict:
        group = self.group_repository.create(body=body)
        return self.response_ok({'id': group.id, 'msg': 'группа создана'})

    def update(self, group_id: int, body: dict) -> dict:
        group = self.group_repository.get_by_id(group_id)
        if not group or not group.creator_id == g.user_id:
            return self.response_not_found('группа не найдена')
        self.group_repository.update(group=group, body=body)
        return self.response_updated('группа обновлена')

    def delete(self, group_id: int) -> dict:
        group = self.group_repository.get_by_id(group_id)
        if not group or not group.creator_id == g.user_id:
            return self.response_not_found('группа не найдена')
        self.group_repository.delete(group)
        return self.response_deleted('группа удалена')

    def get_by_id(self, group_id: int) -> dict:
        group = self.group_repository.get_by_id(group_id)
        if not group:
            return self.response_not_found('группа не найдена')
        return self.response_ok({
            "id": group.id,
            "title": group.title,
            "description": group.description,
            "image": self.get_dict_items(group.image) if group.image else None,
            "creator_id": group.creator_id,
            "user_count": len(group.users),
            "entered": any(user.id == g.user_id for user in group.users)
        })

    def get_all(self, page: int, per_page: int, search: str) -> dict:
        groups: list = self.group_repository.get_all(page=page, per_page=per_page, search=search)
        return self.response_ok({
            'total': groups.total,
            'page': groups.page,
            'pages': groups.pages,
            'per_page': groups.per_page,
            'items': [{
                'id': group.id,
                'title': group.title,
                'description': group.description,
                'image': self.get_dict_items(group.image) if group.image else None,
                "creator_id": group.creator_id,
                "user_count": len(group.users),
                "entered": any(user.id == g.user_id for user in group.users)
            } for group in groups.items]
        })
        