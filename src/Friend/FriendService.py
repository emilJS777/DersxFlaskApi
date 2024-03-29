from src.__Parents.Service import Service
from .IFriendRepo import IFriendRepo
from flask import g

from ..Notification.INotificationRepo import INotificationRepo
from ..Socketio.ISocketio import ISocketio
from ..User.IUserRepo import IUserRepo
from ..__Parents.Repository import Repository


class FriendService(Service, Repository):

    def __init__(self,
                 friend_repository: IFriendRepo,
                 user_repository: IUserRepo,
                 notification_repository: INotificationRepo):

        self.friend_repository: IFriendRepo = friend_repository
        self.user_repository: IUserRepo = user_repository
        self.notification_repository: INotificationRepo = notification_repository

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
            self.notification_repository.create(user_id=body['user_id'], friend_id=friend.id)

            return self.response_created(msg_rus='запрос на дружбу отправлен',
                                         msg_arm='ուղարկվել է ընկերության հարցում',
                                         msg_eng='friend request sent')
        else:
            return self.response_conflict(msg_rus='запрос на дружбу уже был создан',
                                          msg_eng='Friend request has already been created!',
                                          msg_arm='Ընկերության հարցումն արդեն ստեղծվել է')

    def update(self, friend_id: int, user_id: int) -> dict:
        friend = self.friend_repository.get_by_id(friend_id) if friend_id else \
            self.friend_repository.get_by_user_id(user_id)

        if not friend:
            return self.response_not_found(msg_rus='запрос на дружбу был отменен или не найден',
                                           msg_arm='ընկերոջ հարցումը չեղարկվել է կամ չի գտնվել',
                                           msg_eng='friend request was canceled or not found')

        friend = self.friend_repository.update(friend)
        self.notification_repository.delete(friend_id=friend_id)
        # NOTIFICATION
        self.notification_repository.create(friend_id=friend.id, user_id=friend.creator_id)
        return self.response_updated(msg_rus='теперь вы друзья!',
                                     msg_eng='now you are friends!',
                                     msg_arm='այժմ դուք ընկերներ եք!')

    def delete(self, friend_id: int, user_id: int) -> dict:
        friend = self.friend_repository.get_by_id(friend_id) if friend_id else \
            self.friend_repository.get_by_user_id(user_id)

        if not friend:
            return self.response_not_found(msg_rus='запрос на дружбу был отменен или не найден',
                                           msg_arm='ընկերոջ հարցումը չեղարկվել է կամ չի գտնվել',
                                           msg_eng='friend request was canceled or not found')
        self.notification_repository.delete(friend_id=friend.id)
        self.friend_repository.delete(friend)

        if friend.confirmed:
            return self.response_deleted(msg_rus='друг удален',
                                         msg_arm='ընկերը ջնջված է',
                                         msg_eng='friend deleted')
        else:
            return self.response_deleted(msg_rus='запрос на дружбу отменен',
                                         msg_eng='friend request canceled',
                                         msg_arm='ընկերության հարցումը չեղարկվել է')

    def get_by_user_id(self, user_id: int) -> dict:
        friend = self.friend_repository.get_by_user_id(user_id)
        if not friend:
            return self.response_not_found(msg_rus='пользователь не найден ',
                                           msg_arm='user is not found',
                                           msg_eng='oգտագործողը չի գտնվել')
        return self.response_ok(self.get_dict_items(friend))

    # def get_all_requests(self, page: int, per_page: int) -> dict:
    #     friends = self.friend_repository.get_all_requests(page=page, per_page=per_page)
    #     users = self.get_users_by_friends(friends=friends.items, user_id=g.user_id)
    #
    #     return self.response_ok({
    #         'total': friends.total,
    #         'page': friends.page,
    #         'pages': friends.pages,
    #         'per_page': friends.per_page,
    #         'items': [{
    #             'id': user.id,
    #             'name': user.name,
    #             'first_name': user.first_name,
    #             'last_name': user.last_name,
    #             'email_address': user.email_address,
    #             'role_id': user.role_id,
    #             'gender': self.get_dict_items(user.gender),
    #             'image': self.get_dict_items(user.image) if user.image else None
    #         } for user in users]
    #     })

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
                'email': self.get_dict_items(user.email),
                'role_id': user.role_id,
                'gender': self.get_dict_items(user.gender),
                'image': self.get_dict_items(user.image) if user.image else None
            } for user in users]
        })
