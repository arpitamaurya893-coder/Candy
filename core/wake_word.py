class WakeWord:

    def __init__(self):
        self.words = [
            "hey candy",
            "hi candy",
            "hello candy",
            "candy"
        ]

    def detected(self, command):

        if not command:
            return False

        command = command.lower()

        return any(word in command for word in self.words)