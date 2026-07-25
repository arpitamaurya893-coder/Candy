from time import sleep

from core.state import CandyState
from core.state_manager import StateManager


manager = StateManager()

manager.set_state(CandyState.BOOTING)

sleep(2)

manager.set_state(CandyState.WAITING)

sleep(2)

manager.set_state(CandyState.LISTENING)

sleep(2)

manager.set_state(CandyState.THINKING)

sleep(2)

manager.set_state(CandyState.SPEAKING)

sleep(2)

manager.set_state(CandyState.WAITING)