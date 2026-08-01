import threading
import tkinter as tk
import customtkinter as ctk

from gui.ai_core import AICore
from gui.status_bar import StatusBar
from core.wake_word import WakeWord


class CandyWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Theme
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # Window
        self.title("CANDY")
        self.geometry("900x600")
        self.resizable(False, False)
        self.configure(fg_color="#0b0b0b")

        # Layout
        self.grid_columnconfigure(0, weight=1)

        # Title
        self.title_label = ctk.CTkLabel(
            self,
            text="CANDY",
            font=("Segoe UI", 32, "bold"),
            text_color="white"
        )
        self.title_label.grid(row=0, column=0, pady=(30, 10))

        # Canvas
        self.circle = tk.Canvas(
            self,
            width=170,
            height=170,
            bg="#0b0b0b",
            highlightthickness=0
        )
        self.circle.grid(row=1, column=0, pady=20)

        # AI Core
        self.ai = AICore(self.circle)
        self.ai.draw()
        self.ai.pulse()

        # Status Bar
        self.status = StatusBar(self)
        self.status.update_status("💤 Sleeping...")
        self.status.grid(row=2, column=0, pady=(0, 20))

        # Wake Word
        self.wake_word = WakeWord()

        # Start Voice Assistant
        self.voice_thread = threading.Thread(
            target=self.start_assistant,
            daemon=True
        )
        self.voice_thread.start()

    def start_assistant(self):

        from core.listener import Listener
        from core.speaker import Speaker
        from core.brain import Brain

        listener = Listener()
        speaker = Speaker()
        brain = Brain()

        print("🤍 Candy is Online, Boss!")
        print("💤 Waiting for wake word...")

        while True:

            # ---------- Sleeping ----------
            self.after(
                0,
                lambda: self.status.update_status("💤 Sleeping...")
            )

            command = listener.listen()

            if not command:
                continue

            # ---------- Wake Word ----------
            if not self.wake_word.detected(command):
                print("💤 Wake word not detected.")
                continue

            print("✨ Wake word detected!")

            # Check whether command is already included
            wake_words = [
                "hey candy",
                "hi candy",
                "hello candy",
                "candy"
            ]

            command_after_wake = command

            for word in wake_words:

                if word in command_after_wake:

                    command_after_wake = command_after_wake.replace(
                        word,
                        "",
                        1
                    ).strip()

                    break

            # ---------- Wake only ----------
            if not command_after_wake:

                self.after(
                    0,
                    lambda: self.status.update_status("👋 Hello Boss...")
                )

                speaker.speak("Yes Boss?")

                self.after(
                    0,
                    lambda: self.status.update_status("🎤 Listening...")
                )

                command_after_wake = listener.listen()

                if not command_after_wake:
                    continue

            # ---------- Thinking ----------
            self.after(
                0,
                lambda: self.status.update_status("🧠 Thinking...")
            )

            response = brain.process(command_after_wake)

            # ---------- Speaking ----------
            self.after(
                0,
                lambda: self.status.update_status("🗣 Speaking...")
            )

            speaker.speak(response)

            # ---------- Back to Sleep ----------
            self.after(
                0,
                lambda: self.status.update_status("💤 Sleeping...")
            )