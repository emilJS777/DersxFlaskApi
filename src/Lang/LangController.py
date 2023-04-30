from src.__Parents.Controller import Controller
from .LangService import LangService


class LangController(Controller):
    lang_service: LangService = LangService()

    def get(self) -> dict:
        res: dict = self.lang_service.get(lang=self.arguments.get('lang'))
        return res
