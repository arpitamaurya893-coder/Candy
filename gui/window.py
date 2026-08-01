import threading
import tkinter as tk
import customtkinter as ctk

from gui.ai_core import AICore
from gui.status_bar import StatusBar
from core.wake_word import WakeWord


class CandyWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        # ---------- Theme ----------
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # ---------- Window ----------
        self.title("CANDY")
        self.geometry("900x600")
        self.resizable(False, False)
        self.configure(fg_color="#0b0b0b")

        # ---------- Layout ----------
        self.grid_columnconfigure(0, weight=1)

        # ---------- Title ----------
        self.title_label = ctk.CTkLabel(
            self,
            text="CANDY",
            font=("Segoe UI", 32, "bold"),
            text_color="white"
        )

        self.title_label.grid(
            row=0,
            column=0,
            pady=(30, 10)
        )

        # ---------- AI Core Canvas ----------
        self.circle = tk.Canvas(
            self,
            width=170,
            height=170,
            bg="#0b0b0b",
            highlightthickness=0
        )

        self.circle.grid(
            row=1,
            column=0,
            pady=20
        )

        # ---------- AI Core ----------
        self.ai = AICore(self.circle)

        self.ai.draw()
        self.ai.pulse()

        # ---------- Status Bar ----------
        self.status = StatusBar(self)

        self.status.update_status(
            "💤 Sleeping..."
        )

        self.status.grid(
            row=2,
            column=0,
            pady=(0, 20)
        )

        # ---------- Wake Word ----------
        self.wake_word = WakeWord()

        # ---------- Start Assistant ----------
        self.voice_thread = threading.Thread(
            target=self.start_assistant,
            daemon=True
        )

        self.voice_thread.start()

    # =========================================================
    # VOICE ASSISTANT
    # =========================================================

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

            # =================================================
            # SLEEPING
            # =================================================

            self.after(
                0,
                lambda: self.status.update_status(
                    "💤 Sleeping..."
                )
            )

            command = listener.listen()

            if not command:
                continue

            # =================================================
            # CHECK WAKE WORD
            # =================================================

            if not self.wake_word.detected(command):

                print("💤 Wake word not detected.")

                continue

            print("✨ Wake word detected!")

            # =================================================
            # REMOVE WAKE WORD
            # =================================================

            command_after_wake = self.remove_wake_word(command)

            # =================================================
            # WAKE WORD ONLY
            # =================================================

            if not command_after_wake:

                self.after(
                    0,
                    lambda: self.status.update_status(
                        "👋 Hello Boss..."
                    )
                )

                speaker.speak(
                    "Yes Boss?"
                )

                self.after(
                    0,
                    lambda: self.status.update_status(
                        "🎤 Listening..."
                    )
                )

                # Listen for actual command
                command_after_wake = listener.listen()

                if not command_after_wake:

                    self.after(
                        0,
                        lambda: self.status.update_status(
                            "💤 Sleeping..."
                        )
                    )

                    continue

            # =================================================
            # THINKING
            # =================================================

            self.after(
                0,
                lambda: self.status.update_status(
                    "🧠 Thinking..."
                )
            )

            print(
                f"🧠 Processing: {command_after_wake}"
            )

            response = brain.process(
                command_after_wake
            )

            # =================================================
            # SPEAKING
            # =================================================

            self.after(
                0,
                lambda: self.status.update_status(
                    "🗣 Speaking..."
                )
            )

            speaker.speak(
                response
            )

            # =================================================
            # BACK TO SLEEP
            # =================================================

            self.after(
                0,
                lambda: self.status.update_status(
                    "💤 Sleeping..."
                )
            )

            print("💤 Back to sleep.")

    # =========================================================
    # REMOVE WAKE WORD
    # =========================================================

    def remove_wake_word(self, command):

        command = command.lower().strip()

        wake_words = [
            "hey candy",
            "hi candy",
            "hello candy",
            "hay candy",

            "hey cand",
            "hey kandi",
            "hi kandi",
            "hello kandi",

            "candy"
        ]

        # Longest phrases first
        wake_words.sort(
            key=len,
            reverse=True
        )

        for word in wake_words:

            if command.startswith(word):

                command = command[
                    len(word):
                ].strip()

                return command

        return command