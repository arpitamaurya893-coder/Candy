class WakeWord:

    def __init__(self):

        self.words = [
            "hey candy",
            "hi candy",
            "hello candy",
            "hay candy",
            "hey cand",
            "hey kandi",
            "hi kandi",
            "hello kandi",
            "candy"
        ]

    def detected(self, command):

        if not command:
            return False

        command = command.lower().strip()

        for word in self.words:

            if word in command:
                return True

        return False