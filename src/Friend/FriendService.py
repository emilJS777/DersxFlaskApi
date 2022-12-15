from src.__Parents.Service import Service
from .IFriendRepo import IFriendRepo
from flask import g

from ..User.IUserRepo import IUserRepo
from ..__Parents.Repository import Repository


class FriendService(Service, Repository):

    def __init__(self, friend_repository: IFriendRepo, user_repository: IUserRepo):
        self.friend_repository: IFriendRepo = friend_repository
        self.user_repository: IUserRepo = user_repository

    def create(self, body: dict) -> dict:
        self.friend_repository.create(body=body)
        return self.response_created('запрос на дружбу отправлен')

    def update(self, friend_id: int) -> dict:
        friend = self.friend_repository.get_by_id(friend_id)
        if not friend:
            return self.response_not_found('запрос на дружбу был отменен или не найден')

        self.friend_repository.update(friend)
        return self.response_updated('теперь вы друзья!')

    def delete(self, friend_id: int) -> dict:
        friend = self.friend_repository.get_by_id(friend_id)
        if not friend:
            return self.response_not_found('запрос на дружбу был отменен или не найден')
        self.friend_repository.delete(friend)

        if friend.confirmed:
            return self.response_deleted('друг удален!')
        else:
            return self.response_deleted('запрос на дружбу отменен')

    def get_by_user_id(self, user_id: int) -> dict:
        friend = self.friend_repository.get_by_user_id(user_id)
        if not friend:
            return self.response_not_found()
        return self.response_ok(self.get_dict_items(friend))

    def get_all(self, page: int, per_page: int, user_id: int) -> dict:
        friends = self.friend_repository.get_all(page=page, per_page=per_page, user_id=user_id)

        user_ids: list[int] = []
        for friend in friends.items:
            if friend.user_1_id != user_id:
                user_ids.append(friend.user_1_id)
            else:
                user_ids.append(friend.user_2_id)

        users = self.user_repository.get_all_by_ids(user_ids=user_ids)

        return self.response_ok({
            'total': friends.total,
            'page': friends.page,
            'pages': friends.pages,
            'per_page': friends.per_page,
            'items': [{
                'id': user.id,
                'name': user.name,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email_address': user.email_address,
                'role_id': user.role_id,
                'gender': self.get_dict_items(user.gender),
                'image': self.get_dict_items(user.image) if user.image else None
            } for user in users]
        })
