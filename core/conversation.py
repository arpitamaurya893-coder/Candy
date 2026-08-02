import json
import os


class Conversation:

    def __init__(self):

        self.file = "config/conversation.json"

        self.last_command = None
        self.last_response = None
        self.topic = None

        self.load()


    # =========================================================
    # LOAD CONVERSATION
    # =========================================================

    def load(self):

        try:

            if os.path.exists(self.file):

                with open(
                    self.file,
                    "r",
                    encoding="utf-8"
                ) as f:

                    data = json.load(f)

                    self.last_command = data.get(
                        "last_command"
                    )

                    self.last_response = data.get(
                        "last_response"
                    )

                    self.topic = data.get(
                        "topic"
                    )

        except Exception as e:

            print(
                f"⚠️ Conversation load error: {e}"
            )


    # =========================================================
    # SAVE CONVERSATION
    # =========================================================

    def save(self):

        try:

            os.makedirs(
                "config",
                exist_ok=True
            )

            data = {

                "last_command":
                    self.last_command,

                "last_response":
                    self.last_response,

                "topic":
                    self.topic

            }

            with open(
                self.file,
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(
                    data,
                    f,
                    indent=4,
                    ensure_ascii=False
                )

        except Exception as e:

            print(
                f"⚠️ Conversation save error: {e}"
            )


    # =========================================================
    # REMEMBER
    # =========================================================

    def remember(
        self,
        command,
        response=None,
        topic=None
    ):

        self.last_command = command

        if response is not None:

            self.last_response = response

        if topic is not None:

            self.topic = topic

        self.save()


    # =========================================================
    # GET LAST COMMAND
    # =========================================================

    def get_last_command(self):

        return self.last_command


    # =========================================================
    # GET LAST RESPONSE
    # =========================================================

    def get_last_response(self):

        return self.last_response


    # =========================================================
    # GET CURRENT TOPIC
    # =========================================================

    def get_topic(self):

        return self.topic


    # =========================================================
    # CLEAR CONVERSATION
    # =========================================================

    def clear(self):

        self.last_command = None
        self.last_response = None
        self.topic = None

        self.save()