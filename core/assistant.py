from core.listener import Listener
from core.speaker import Speaker
from core.brain import Brain
from core.state import CandyState
from core.state_manager import StateManager


class CandyAssistant:

    def __init__(self):

        self.listener = Listener()
        self.speaker = Speaker()
        self.brain = Brain()
        self.state = StateManager()

    def process(self):

        # Listening
        self.state.set_state(CandyState.LISTENING)

        command = self.listener.listen()

        if not command:

            self.state.set_state(CandyState.WAITING)
            return

        # Thinking
        self.state.set_state(CandyState.THINKING)

        response = self.brain.process(command)

        # Speaking
        self.state.set_state(CandyState.SPEAKING)

        print(response)

        self.speaker.speak(response)

        # Back to Waiting
        self.state.set_state(CandyState.WAITING)