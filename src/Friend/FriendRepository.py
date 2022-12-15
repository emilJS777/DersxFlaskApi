from sqlalchemy import or_, and_
from .IFriendRepo import IFriendRepo
from .FriendModel import Friend
from flask import g


class FriendRepository(IFriendRepo):

    def create(self, body: dict):
        friend: Friend = Friend()
        friend.user_1_id = g.user_id
        friend.user_2_id = body['user_id']
        friend.creator_id = g.user_id
        friend.save_db()

    def update(self, friend: Friend):
        friend.confirmed = True
        friend.update_db()

    def delete(self, friend: Friend):
        friend.delete_db()

    def get_by_user_id(self, user_id: int) -> Friend:
        friend: Friend = Friend.query.filter(or_(
            and_(Friend.user_1_id == user_id, Friend.user_2_id == g.user_id),
            and_(Friend.user_2_id == user_id, Friend.user_1_id == g.user_id),
        )).first()
        return friend

    def get_by_id(self, friend_id: int) -> Friend:
        friend: Friend = Friend.query\
            .filter_by(id=friend_id)\
            .filter(or_(Friend.user_1_id == g.user_id, Friend.user_2_id == g.user_id))\
            .first()
        return friend

    def get_all(self, page: int, per_page: int, user_id: int):
        friends = Friend.query\
            .filter_by(confirmed=True)\
            .filter(or_(
                Friend.user_1_id == user_id,
                Friend.user_2_id == user_id
            )).paginate(page=page, per_page=per_page)
        return friends
