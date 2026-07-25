from core.listener import Listener
from core.speaker import Speaker
from core.brain import Brain


listener = Listener()
speaker = Speaker()
brain = Brain()


print("🤍 Candy is Online, Boss!")

while True:

    command = listener.listen()

    if not command:
        continue

    response = brain.process(command)

    print(response)

    speaker.speak(response)