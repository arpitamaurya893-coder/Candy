class Conversation:

    def __init__(self):

        # Last command spoken by Boss
        self.last_command = None

        # Last response given by Candy
        self.last_response = None

        # Current topic of conversation
        self.topic = None


    # ---------- Save Conversation ----------

    def remember(self, command, response=None, topic=None):

        self.last_command = command

        if response:
            self.last_response = response

        if topic:
            self.topic = topic


    # ---------- Get Last Command ----------

    def get_last_command(self):

        return self.last_command


    # ---------- Get Last Response ----------

    def get_last_response(self):

        return self.last_response


    # ---------- Get Current Topic ----------

    def get_topic(self):

        return self.topic


    # ---------- Clear Conversation ----------

    def clear(self):

        self.last_command = None
        self.last_response = None
        self.topic = None