from src.__Parents.Service import Service
from .IFriendRepo import IFriendRepo
from flask import g
from ..Socketio.ISocketio import ISocketio
from ..User.IUserRepo import IUserRepo
from ..__Parents.Repository import Repository


class FriendService(Service, Repository):

    def __init__(self, friend_repository: IFriendRepo, user_repository: IUserRepo, socket_io: ISocketio):
        self.friend_repository: IFriendRepo = friend_repository
        self.user_repository: IUserRepo = user_repository
        self.socket_io: ISocketio = socket_io

    def get_users_by_friends(self, friends: list, user_id: int):
        user_ids: list[int] = []
        for friend in friends:
            if friend.user_1_id != user_id:
                user_ids.append(friend.user_1_id)
            else:
                user_ids.append(friend.user_2_id)
        return self.user_repository.get_all_by_ids(user_ids=user_ids)

    def create(self, body: dict) -> dict:
        if not self.friend_repository.get_by_user_id(user_id=body['user_id']):
            friend = self.friend_repository.create(body=body)
            users = self.get_users_by_friends(friends=[friend], user_id=body['user_id'])
            socket_data = {
                'total': 1,
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
            }
            self.socket_io.send(emit_name='friend_request', data=socket_data, user_id=body['user_id'])
            return self.response_created('запрос на дружбу отправлен')
        else:
            return self.response_conflict('запрос на дружбу уже был создан !')

    def update(self, friend_id: int, user_id: int) -> dict:
        friend = self.friend_repository.get_by_id(friend_id) if friend_id else \
            self.friend_repository.get_by_user_id(user_id)

        if not friend:
            return self.response_not_found('запрос на дружбу был отменен или не найден')

        self.friend_repository.update(friend)
        users = self.user_repository.get_all_by_ids(user_ids=[friend.user_1_id, friend.user_2_id])

        socket_data_user_1 = {
            'total': 1,
            'items': [{
                'id': users[0].id,
                'confirmed': True,
                'name': users[0].name,
                'first_name': users[0].first_name,
                'last_name': users[0].last_name,
                'email_address': users[0].email_address,
                'role_id': users[0].role_id,
                'gender': self.get_dict_items(users[0].gender),
                'image': self.get_dict_items(users[0].image) if users[0].image else None
            }]
        }

        socket_data_user_2 = {
            'total': 1,
            'items': [{
                'id': users[1].id,
                'confirmed': True,
                'name': users[1].name,
                'first_name': users[1].first_name,
                'last_name': users[1].last_name,
                'email_address': users[1].email_address,
                'role_id': users[1].role_id,
                'gender': self.get_dict_items(users[1].gender),
                'image': self.get_dict_items(users[1].image) if users[1].image else None
            }]
        }

        self.socket_io.send(emit_name='friend_request', data=socket_data_user_2, user_id=users[0].id)
        self.socket_io.send(emit_name='friend_request', data=socket_data_user_1, user_id=users[1].id)
        return self.response_updated('теперь вы друзья!')

    def delete(self, friend_id: int, user_id: int) -> dict:
        friend = self.friend_repository.get_by_id(friend_id) if friend_id else \
            self.friend_repository.get_by_user_id(user_id)

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

    def get_all_requests(self, page: int, per_page: int) -> dict:
        friends = self.friend_repository.get_all_requests(page=page, per_page=per_page)
        users = self.get_users_by_friends(friends=friends.items, user_id=g.user_id)

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

    def get_all(self, page: int, per_page: int, user_id: int) -> dict:
        friends = self.friend_repository.get_all(page=page, per_page=per_page, user_id=user_id)
        users = self.get_users_by_friends(friends=friends.items, user_id=user_id)

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
