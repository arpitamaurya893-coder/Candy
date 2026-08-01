import json
import os


class Memory:

    def __init__(self):

        self.name = "Candy"
        self.owner = "Boss"

        self.personality = {
            "english": {
                "greeting": "Hello Boss.",
                "waiting": "I'm listening.",
                "goodbye": "Okay Boss. I'll wait."
            },

            "hindi": {
                "greeting": "Namaste Boss.",
                "waiting": "Main sun rahi hoon.",
                "goodbye": "Theek hai Boss. Main wait karti hoon."
            },

            "hinglish": {
                "greeting": "Hello Boss 😊",
                "waiting": "Main sun rahi hoon Boss.",
                "goodbye": "Theek hai Boss. Jab zarurat ho bula lena."
            }
        }

        # Memory file
        self.file = "config/memory.json"

        # Stored memories
        self.data = {
            "owner_name": None,
            "facts": {}
        }

        self.load()

    def load(self):

        try:

            if os.path.exists(self.file):

                with open(
                    self.file,
                    "r",
                    encoding="utf-8"
                ) as f:

                    self.data = json.load(f)

        except Exception as e:

            print(f"⚠️ Memory load error: {e}")

    def save(self):

        try:

            os.makedirs("config", exist_ok=True)

            with open(
                self.file,
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(
                    self.data,
                    f,
                    indent=4,
                    ensure_ascii=False
                )

        except Exception as e:

            print(f"⚠️ Memory save error: {e}")

    def remember(self, key, value):

        self.data["facts"][key] = value

        self.save()

    def recall(self, key):

        return self.data["facts"].get(key)