from enum import Enum


class CandyState(Enum):

    BOOTING = "Booting"

    WAITING = "Waiting"

    LISTENING = "Listening"

    THINKING = "Thinking"

    SPEAKING = "Speaking"

    SLEEPING = "Sleeping"