from core.memory import Memory
from core.language import Language
from core.intent import INTENTS
from core.responses import RESPONSES
from core.app_control import AppControl
from core.search import Search


class Brain:

    def __init__(self):
        self.memory = Memory()
        self.language = Language()
        self.app = AppControl()
        self.search = Search()

    def process(self, command):

        lang = self.language.detect(command)
        command = command.lower().strip()

        # ---------- App Control ----------
        app_response = self.app.execute(command)

        if app_response:
            return app_response

        # ---------- Smart Search ----------
        search_response = self.search.execute(command)

        if search_response:
            return search_response

        # ---------- Intent Detection ----------
        for intent, phrases in INTENTS.items():

            for phrase in phrases:

                phrase = phrase.lower().strip()

                # Exact Match
                if command == phrase:
                    return RESPONSES[intent][lang]

                # Full Word Match
                if f" {phrase} " in f" {command} ":
                    return RESPONSES[intent][lang]

        return "Boss... mujhe ye poori tarah samajh nahi aaya. Ek baar aur bolengi?"