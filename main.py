from core.listener import Listener
from core.speaker import Speaker
from core.brain import Brain
from core.wake_word import WakeWord


listener = Listener()
speaker = Speaker()
brain = Brain()
wake = WakeWord()

awake = False

print("🤍 Candy is Online, Boss!")

while True:

    command = listener.listen()

    if not command:
        continue

    # Wake Word Check
    if not awake:

        if wake.detected(command):
            awake = True
            response = "Yes Boss, I'm listening."
            print(response)
            speaker.speak(response)

        continue

    # Sleep Command
    if command in [
        "sleep",
        "go to sleep",
        "bye",
        "goodbye"
    ]:

        awake = False

        response = "Okay Boss. Call me whenever you need me."

        print(response)
        speaker.speak(response)

        continue

    # Normal Conversation
    response = brain.process(command)

    print(response)

    speaker.speak(response)