from core.state import CandyState


class StateManager:

    def __init__(self):

        self.current_state = CandyState.BOOTING
        self.callback = None

    def register_callback(self, callback):

        self.callback = callback

    def set_state(self, state):

        self.current_state = state

        print(f"🤍 Candy State -> {state.value}")

        if self.callback:
            self.callback(state)

    def get_state(self):

        return self.current_state