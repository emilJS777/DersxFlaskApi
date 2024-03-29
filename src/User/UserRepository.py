from sqlalchemy import or_, not_
from src.__Parents.Repository import Repository
from .IUserRepo import IUserRepo
from .UserModel import User
from flask_bcrypt import generate_password_hash
from src.Skill.SkillModel import Skill
from src.Category.CategoryModel import Category
from ..Email.EmailModel import Email
from ..Group.GroupModel import Group
from src import db


class UserRepository(Repository, IUserRepo):
    user: User = User

    def create(self, body: dict, admin: bool = False) -> User:
        user = self.user()
        user.name = body['name']
        user.admin = admin
        user.password_hash = generate_password_hash(body['password'])
        user.first_name = body['first_name'].title()
        user.last_name = body['last_name'].title()
        user.date_birth = body['date_birth'].split('T')[0]
        user.region = body['region']
        user.gender_id = body['gender_id']
        user.save_db()
        return user

    def update(self, user_id: int, body: dict) -> dict:
        user = self.user.query.filter_by(id=user_id).first()

        if body.get('name'):
            user.name = body['name']

        if body.get('first_name'):
            user.first_name = body['first_name']

        if body.get('last_name'):
            user.last_name = body['last_name']

        if body.get('date_birth'):
            user.date_birth = body['date_birth'].split('T')[0]

        if body.get('region'):
            user.region = body['region']

        if body.get('role_id'):
            user.role_id = body['role_id']

        if body.get('image_path'):
            user.image_path = body['image_path']

        if body.get('gender_id'):
            user.gender_id = body['gender_id']

        user.update_db()
        return self.get_dict_items(user)

    def update_role(self, user_id: int, role_id: int) -> dict:
        user = self.user.query.filter_by(id=user_id).first()
        user.role_id = role_id
        user.update_db()
        return self.get_dict_items(user)

    def delete(self, user_id: int) -> dict:
        user = self.user.query.filter_by(id=user_id).first()
        user.delete_db()
        return self.get_dict_items(user)

    def get_by_id(self, user_id: int) -> User:
        user = self.user.query.filter_by(id=user_id).first()
        return user

    def get_by_name(self, name: str) -> User:
        user = self.user.query.filter_by(name=name).first()
        return user

    def get_by_name_or_email(self, name_or_email: str):
        user = self.user.query.join(User.email).filter(or_(User.name == name_or_email, Email.address == name_or_email)).first()
        return user

    def get_by_name_exclude_id(self, user_id: int, name: str) -> dict:
        user = self.user.query.filter(self.user.id != user_id, self.user.name == name).first()
        return self.get_dict_items(user)

    def get_all(self, page: int, per_page: int, rubric_id: int or None, role_id: int or None, category_ids: list[int] or None,
                search: str or None, group_id: int or None, not_group_id: int or None) -> dict:
        users = self.user.query\
            .where(User.skills.any(Skill.rubric_id.in_([rubric_id])) if rubric_id else User.id.isnot(None))\
            .where(User.skills.any(Skill.categories.any(Category.id.in_(category_ids))) if category_ids else User.id.isnot(None))\
            .filter(or_(User.last_name.like(f"%{search}%"), User.first_name.like(f"%{search}%")) if search else User.id.isnot(None)) \
            .filter(User.groups.any(Group.id == group_id) if group_id else User.id.isnot(None))\
            .filter(not_(User.groups.any(Group.id == not_group_id)))\
            .paginate(page=page, per_page=per_page)
        return users

    def get_all_by_ids(self, user_ids: list[int]) -> list[User]:
        users: list[User] = User.query.filter(User.id.in_(user_ids)).all()
        return users

    def get_count(self) -> int:
        users_count = db.session.query(User).count()
        return users_count


