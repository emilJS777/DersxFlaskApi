from abc import ABC, abstractmethod


class IUserRepo(ABC):

    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, user_id: int, body: dict):
        pass

    @abstractmethod
    def delete(self, user_id: int):
        pass

    @abstractmethod
    def get_by_id(self, user_id: int):
        pass

    @abstractmethod
    def get_by_name(self, name: str):
        pass

    @abstractmethod
    def get_by_email_address_exclude_id(self, user_id: int, email_address: str):
        pass

    @abstractmethod
    def get_by_name_exclude_id(self, user_id: int, name: str):
        pass

    @abstractmethod
    def get_all(self, page: int, per_page: int, rubric_id: int or None, role_id: int or None, category_ids: list[int], search: str or None):
        pass









