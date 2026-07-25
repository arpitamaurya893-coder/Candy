from core.memory import Memory
from core.language import Language
from core.intent import INTENTS
from core.responses import RESPONSES


class Brain:

    def __init__(self):
        self.memory = Memory()
        self.language = Language()

    def process(self, command):

        lang = self.language.detect(command)
        command = command.lower()

        # Intent Detection
        for intent, phrases in INTENTS.items():

            for phrase in phrases:

                if phrase in command:

                    return RESPONSES[intent][lang]

        return "Boss... mujhe ye poori tarah samajh nahi aaya. Ek baar aur bolengi?"