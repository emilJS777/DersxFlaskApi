from src import app
from src.__Parents.Service import Service
import json


class LangService(Service):
    def get(self, lang: str) -> dict:
        with open(f'{app.config.get("LANGS")}/{lang}.json', 'r') as f:
            data = f.read()
        return self.response_ok(data)
