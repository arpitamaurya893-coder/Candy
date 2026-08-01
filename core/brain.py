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


        # =====================================================
        # APP CONTROL
        # =====================================================

        app_response = self.app.execute(command)

        if app_response:
            return app_response


        # =====================================================
        # SMART SEARCH
        # =====================================================

        search_response = self.search.execute(command)

        if search_response:
            return search_response


        # =====================================================
        # MEMORY - REMEMBER NAME
        # =====================================================

        name_patterns = [

            "my name is ",
            "my name's ",
            "mera naam ",
            "mera naam hai "

        ]


        for pattern in name_patterns:

            if command.startswith(pattern):

                name = command[
                    len(pattern):
                ].strip()


                if name:

                    name = name.title()

                    self.memory.remember(
                        "owner_name",
                        name
                    )

                    return (
                        f"Okay Boss. "
                        f"I will remember your name is {name}."
                    )


        # =====================================================
        # MEMORY - RECALL NAME
        # =====================================================

        name_questions = [

            "what is my name",
            "what's my name",
            "what is my name candy",
            "what's my name candy",
            "mera naam kya hai",
            "mera naam kya hai candy",
            "do you know my name",
            "do you remember my name"

        ]


        if command in name_questions:

            saved_name = self.memory.recall(
                "owner_name"
            )


            if saved_name:

                return (
                    f"Your name is "
                    f"{saved_name}, Boss. 😊"
                )


            return (
                "Boss, you haven't told me "
                "your name yet."
            )


        # =====================================================
        # INTENT DETECTION
        # =====================================================

        for intent, phrases in INTENTS.items():

            for phrase in phrases:

                phrase = phrase.lower().strip()


                # Exact Match
                if command == phrase:

                    return RESPONSES[intent][lang]


                # Full Word Match
                if f" {phrase} " in f" {command} ":

                    return RESPONSES[intent][lang]


        # =====================================================
        # UNKNOWN COMMAND
        # =====================================================

        return (
            "Boss... mujhe ye poori tarah "
            "samajh nahi aaya. Ek baar aur bolengi?"
        )