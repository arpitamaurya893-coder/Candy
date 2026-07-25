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