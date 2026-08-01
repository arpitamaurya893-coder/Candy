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

                name = command[len(pattern):].strip()

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
        # MEMORY - REMEMBER FACTS
        # =====================================================

        fact_patterns = {

            "i live in ": "location",
            "i live at ": "location",
            "main ": "custom",
            "my favorite color is ": "favorite_color",
            "my favourite color is ": "favorite_color",
            "my favorite colour is ": "favorite_color",
            "my favourite colour is ": "favorite_color",
            "my favorite food is ": "favorite_food",
            "my favourite food is ": "favorite_food",
            "my hobby is ": "hobby",
            "my college is ": "college",
            "my city is ": "location"

        }


        for pattern, key in fact_patterns.items():

            if command.startswith(pattern):

                value = command[len(pattern):].strip()

                if value:

                    value = value.strip(" .!?")

                    self.memory.remember(
                        key,
                        value
                    )

                    if key == "location":

                        return (
                            f"Okay Boss. "
                            f"I will remember that "
                            f"you live in {value.title()}."
                        )

                    if key == "favorite_color":

                        return (
                            f"Okay Boss. "
                            f"I will remember that "
                            f"your favorite color is {value.title()}."
                        )

                    if key == "favorite_food":

                        return (
                            f"Okay Boss. "
                            f"I will remember that "
                            f"your favorite food is {value.title()}."
                        )

                    if key == "hobby":

                        return (
                            f"Okay Boss. "
                            f"I will remember that "
                            f"your hobby is {value.title()}."
                        )

                    if key == "college":

                        return (
                            f"Okay Boss. "
                            f"I will remember that "
                            f"your college is {value.title()}."
                        )


        # =====================================================
        # MEMORY - RECALL FACTS
        # =====================================================

        memory_questions = {

            "where do i live": "location",
            "where do i live candy": "location",
            "what is my favorite color": "favorite_color",
            "what's my favorite color": "favorite_color",
            "what is my favourite color": "favorite_color",
            "what is my favorite food": "favorite_food",
            "what's my favorite food": "favorite_food",
            "what is my hobby": "hobby",
            "what's my hobby": "hobby",
            "what is my college": "college",
            "what's my college": "college",
            "which college do i go to": "college"

        }


        if command in memory_questions:

            key = memory_questions[command]

            value = self.memory.recall(key)

            if value:

                if key == "location":

                    return (
                        f"You live in {value.title()}, Boss. 😊"
                    )

                if key == "favorite_color":

                    return (
                        f"Your favorite color is "
                        f"{value.title()}, Boss. 😊"
                    )

                if key == "favorite_food":

                    return (
                        f"Your favorite food is "
                        f"{value.title()}, Boss. 😊"
                    )

                if key == "hobby":

                    return (
                        f"Your hobby is "
                        f"{value.title()}, Boss. 😊"
                    )

                if key == "college":

                    return (
                        f"Your college is "
                        f"{value.title()}, Boss. 😊"
                    )

            return (
                "Boss, you haven't told me "
                "that yet."
            )


        # =====================================================
        # MEMORY - SHOW ALL MEMORIES
        # =====================================================

        show_memory_commands = [

            "what do you remember about me",
            "what do you remember",
            "what do you know about me",
            "meri memories batao",
            "mere baare mein kya yaad hai"

        ]


        if command in show_memory_commands:

            memories = self.memory.get_all_memories()

            if not memories:

                return (
                    "Boss, I don't have any "
                    "personal memories saved yet."
                )

            result = "Boss, I remember: "

            memory_list = []

            for key, value in memories.items():

                if key == "location":
                    memory_list.append(
                        f"you live in {value.title()}"
                    )

                elif key == "favorite_color":
                    memory_list.append(
                        f"your favorite color is {value.title()}"
                    )

                elif key == "favorite_food":
                    memory_list.append(
                        f"your favorite food is {value.title()}"
                    )

                elif key == "hobby":
                    memory_list.append(
                        f"your hobby is {value.title()}"
                    )

                elif key == "college":
                    memory_list.append(
                        f"your college is {value.title()}"
                    )

                else:
                    memory_list.append(
                        f"{key} is {value}"
                    )

            result += ", ".join(memory_list) + "."

            return result


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