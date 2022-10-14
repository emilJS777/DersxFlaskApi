from abc import ABC, abstractmethod
from .SkillModel import Skill


class ISkillRepo(ABC):
    @abstractmethod
    def create(self, body: dict, categories: list):
        pass

    @abstractmethod
    def update(self, skill: Skill, body: dict, categories: list):
        pass

    @abstractmethod
    def delete(self, skill: Skill):
        pass

    @abstractmethod
    def get_by_id(self, skill_id: int) -> Skill:
        pass

    @abstractmethod
    def get_all(self, user_id: int) -> list[Skill]:
        pass
