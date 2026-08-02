from core.memory import Memory
from core.language import Language
from core.intent import INTENTS
from core.responses import RESPONSES
from core.app_control import AppControl
from core.search import Search
from core.conversation import Conversation


class Brain:

    def __init__(self):

        self.memory = Memory()
        self.language = Language()
        self.app = AppControl()
        self.search = Search()
        self.conversation = Conversation()

        print("🧠 Conversation memory ready.")


    # =========================================================
    # SAVE CONVERSATION
    # =========================================================

    def save_conversation(self, command, response):

        self.conversation.remember(
            command=command,
            response=response
        )


    # =========================================================
    # MAIN PROCESS
    # =========================================================

    def process(self, command):

        original_command = command

        # -----------------------------------------
        # Save previous command BEFORE processing
        # -----------------------------------------

        previous_command = self.conversation.get_last_command()

        response = self._process(
            original_command,
            previous_command
        )

        # -----------------------------------------
        # Save CURRENT command after processing
        # -----------------------------------------

        self.save_conversation(
            original_command,
            response
        )

        return response


    # =========================================================
    # INTERNAL PROCESS
    # =========================================================

    def _process(self, command, previous_command=None):

        lang = self.language.detect(command)

        command = command.lower().strip()


        # =====================================================
        # CONVERSATION MEMORY
        # =====================================================

        if command in [

            "what did i just say",
            "what did i say",
            "what did i just tell you",
            "what did i tell you",
            "what was my last message",
            "what was my last command",
            "maine abhi kya kaha",
            "maine abhi kya bola",
            "maine kya kaha",
            "maine kya bola"

        ]:

            if previous_command:

                return (
                    f'You just said "{previous_command}", Boss. 😊'
                )

            return (
                "Boss, I don't remember what you just said."
            )


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
        # MEMORY - FORGET EVERYTHING
        # =====================================================

        forget_all_commands = [

            "forget everything",
            "forget all memories",
            "forget all my memories",
            "forget everything about me",
            "clear my memory",
            "clear all memories",
            "meri saari memories bhool jao",
            "sab kuch bhool jao",
            "mujhe bhool jao"

        ]

        if command in forget_all_commands:

            self.memory.data["owner_name"] = None
            self.memory.data["facts"] = {}

            self.memory.save()

            return (
                "Okay Boss. "
                "I have forgotten all your personal memories. 🧹🧠"
            )


        # =====================================================
        # MEMORY - FORGET NAME
        # =====================================================

        forget_name_commands = [

            "forget my name",
            "forget my name candy",
            "don't remember my name",
            "do not remember my name",
            "forget my name please",
            "mera naam bhool jao",
            "mera naam yaad mat rakhna"

        ]

        if command in forget_name_commands:

            if self.memory.data.get("owner_name"):

                self.memory.data["owner_name"] = None

                self.memory.save()

                return (
                    "Okay Boss. "
                    "I have forgotten your name. 🧹"
                )

            return (
                "Boss, I don't have your name "
                "saved in my memory."
            )


        # =====================================================
        # MEMORY - FORGET FACTS
        # =====================================================

        forget_patterns = {

            "forget where i live": "location",
            "forget my location": "location",
            "forget my city": "location",

            "forget my favorite color": "favorite_color",
            "forget my favourite color": "favorite_color",
            "forget my favorite colour": "favorite_color",
            "forget my favourite colour": "favorite_color",

            "forget my favorite food": "favorite_food",
            "forget my favourite food": "favorite_food",

            "forget my hobby": "hobby",

            "forget my college": "college",

            "forget my favorite singer": "favorite_singer",
            "forget my favourite singer": "favorite_singer",

            "forget my favorite song": "favorite_song",
            "forget my favourite song": "favorite_song",

            "forget my favorite actor": "favorite_actor",
            "forget my favourite actor": "favorite_actor",

            "forget my favorite actress": "favorite_actress",
            "forget my favourite actress": "favorite_actress",

            "forget my favorite movie": "favorite_movie",
            "forget my favourite movie": "favorite_movie",

            "forget my favorite game": "favorite_game",
            "forget my favourite game": "favorite_game",

            "forget my favorite subject": "favorite_subject",
            "forget my favourite subject": "favorite_subject",

            "forget my career goal": "career_goal",
            "forget my dream company": "dream_company"

        }


        if command in forget_patterns:

            key = forget_patterns[command]

            forgotten = self.memory.forget(key)

            if forgotten:

                return (
                    f"Okay Boss. "
                    f"I have forgotten your "
                    f"{self.memory_label(key)}. 🧹"
                )

            return (
                "Boss, I don't have that information "
                "saved in my memory."
            )


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

            saved_name = self.memory.recall("owner_name")

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

            # Location
            "i live in ": "location",
            "i live at ": "location",
            "my city is ": "location",

            # Education
            "my college is ": "college",
            "my course is ": "course",
            "my degree is ": "degree",

            "my favorite subject is ": "favorite_subject",
            "my favourite subject is ": "favorite_subject",

            # Favorites
            "my favorite color is ": "favorite_color",
            "my favourite color is ": "favorite_color",
            "my favorite colour is ": "favorite_color",
            "my favourite colour is ": "favorite_color",

            "my favorite food is ": "favorite_food",
            "my favourite food is ": "favorite_food",

            "my favorite singer is ": "favorite_singer",
            "my favourite singer is ": "favorite_singer",

            "my favorite song is ": "favorite_song",
            "my favourite song is ": "favorite_song",

            "my favorite actor is ": "favorite_actor",
            "my favourite actor is ": "favorite_actor",

            "my favorite actress is ": "favorite_actress",
            "my favourite actress is ": "favorite_actress",

            "my favorite movie is ": "favorite_movie",
            "my favourite movie is ": "favorite_movie",

            "my favorite game is ": "favorite_game",
            "my favourite game is ": "favorite_game",

            # Personal
            "my hobby is ": "hobby",

            # Career
            "my career goal is ": "career_goal",
            "my career is ": "career_goal",
            "my dream company is ": "dream_company",
            "my goal is ": "goal"

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

                    return (
                        f"Okay Boss. "
                        f"I will remember that "
                        f"{self.memory_label(key)} "
                        f"is {value.title()}."
                    )


        # =====================================================
        # MEMORY - RECALL FACTS
        # =====================================================

        memory_questions = {

            # Location
            "where do i live": "location",
            "where do i live candy": "location",
            "what is my location": "location",
            "what's my location": "location",
            "what is my city": "location",
            "what's my city": "location",

            # Education
            "what is my college": "college",
            "what's my college": "college",
            "which college do i go to": "college",

            "what is my course": "course",
            "what's my course": "course",

            "what is my degree": "degree",
            "what's my degree": "degree",

            "what is my favorite subject": "favorite_subject",
            "what's my favorite subject": "favorite_subject",
            "what is my favourite subject": "favorite_subject",
            "what's my favourite subject": "favorite_subject",

            # Color
            "what is my favorite color": "favorite_color",
            "what's my favorite color": "favorite_color",
            "what is my favourite color": "favorite_color",
            "what's my favourite color": "favorite_color",
            "what is my favorite colour": "favorite_color",
            "what's my favorite colour": "favorite_color",
            "what is my favourite colour": "favorite_color",
            "what's my favourite colour": "favorite_color",

            # Food
            "what is my favorite food": "favorite_food",
            "what's my favorite food": "favorite_food",
            "what is my favourite food": "favorite_food",
            "what's my favourite food": "favorite_food",

            # Music
            "what is my favorite singer": "favorite_singer",
            "what's my favorite singer": "favorite_singer",
            "what is my favourite singer": "favorite_singer",
            "what's my favourite singer": "favorite_singer",

            "what is my favorite song": "favorite_song",
            "what's my favorite song": "favorite_song",
            "what is my favourite song": "favorite_song",
            "what's my favourite song": "favorite_song",

            # Movies
            "what is my favorite actor": "favorite_actor",
            "what's my favorite actor": "favorite_actor",
            "what is my favourite actor": "favorite_actor",
            "what's my favourite actor": "favorite_actor",

            "what is my favorite actress": "favorite_actress",
            "what's my favorite actress": "favorite_actress",
            "what is my favourite actress": "favorite_actress",
            "what's my favourite actress": "favorite_actress",

            "what is my favorite movie": "favorite_movie",
            "what's my favorite movie": "favorite_movie",
            "what is my favourite movie": "favorite_movie",
            "what's my favourite movie": "favorite_movie",

            # Game
            "what is my favorite game": "favorite_game",
            "what's my favorite game": "favorite_game",
            "what is my favourite game": "favorite_game",
            "what's my favourite game": "favorite_game",

            # Hobby
            "what is my hobby": "hobby",
            "what's my hobby": "hobby",

            # Career
            "what is my career goal": "career_goal",
            "what's my career goal": "career_goal",

            "what is my dream company": "dream_company",
            "what's my dream company": "dream_company",

            "what is my goal": "goal",
            "what's my goal": "goal"

        }


        if command in memory_questions:

            key = memory_questions[command]

            value = self.memory.recall(key)

            if value:

                return (
                    f"Your {self.memory_label(key)} "
                    f"is {value.title()}, Boss. 😊"
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

                memory_list.append(
                    f"your {self.memory_label(key)} "
                    f"is {value.title()}"
                )

            result += ", ".join(memory_list) + "."

            return result


        # =====================================================
        # INTENT DETECTION
        # =====================================================

        for intent, phrases in INTENTS.items():

            for phrase in phrases:

                phrase = phrase.lower().strip()

                if command == phrase:

                    return RESPONSES[intent][lang]

                if f" {phrase} " in f" {command} ":

                    return RESPONSES[intent][lang]


        # =====================================================
        # UNKNOWN COMMAND
        # =====================================================

        return (
            "Boss... mujhe ye poori tarah "
            "samajh nahi aaya. Please ek baar aur bolengi?"
        )


    # =========================================================
    # MEMORY LABEL
    # =========================================================

    def memory_label(self, key):

        labels = {

            "location": "location",
            "college": "college",
            "course": "course",
            "degree": "degree",

            "favorite_color": "favorite color",
            "favorite_food": "favorite food",
            "favorite_singer": "favorite singer",
            "favorite_song": "favorite song",

            "favorite_actor": "favorite actor",
            "favorite_actress": "favorite actress",
            "favorite_movie": "favorite movie",
            "favorite_game": "favorite game",

            "favorite_subject": "favorite subject",
            "hobby": "hobby",

            "career_goal": "career goal",
            "dream_company": "dream company",
            "goal": "goal"

        }

        return labels.get(key, key)