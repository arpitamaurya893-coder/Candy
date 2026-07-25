import asyncio
import edge_tts
import pygame
import tempfile
import os


class Speaker:

    def __init__(self):
        pygame.mixer.init()

    def speak(self, text):

        print(f"🤍 Candy: {text}")

        asyncio.run(self._speak(text))

    async def _speak(self, text):

        # Hindi ya English voice choose karo
        lower = text.lower()

        hindi_words = [
            "hai", "ho", "aap", "main", "mera", "meri",
            "mujhe", "naam", "kya", "kaise", "kaisi"
        ]

        voice = "en-US-AriaNeural"

        if any(word in lower for word in hindi_words):
            voice = "hi-IN-SwaraNeural"

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            filename = f.name

        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(filename)

        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            await asyncio.sleep(0.1)

        pygame.mixer.music.unload()
        os.remove(filename)