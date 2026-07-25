import tkinter as tk
import customtkinter as ctk
from gui.ai_core import AICore
from gui.status_bar import StatusBar


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

        # Create AI Core
        self.ai = AICore(self.circle)
        self.ai.draw()

        
        # Status Bar
        self.status = StatusBar(self)
        self.status.update_status("🤍 Waiting...")
        self.status.grid(row=2, column=0, pady=(0, 20))

    def create_ai_core(self):
        # Outer Ring
        self.circle.create_oval(
            20, 20,
            150, 150,
            outline="white",
            width=2
        )

        # Main Core
        self.ai_core = self.circle.create_oval(
            35, 35,
            135, 135,
            fill="white",
            outline=""
        )

        # Center Dot
        self.circle.create_oval(
            80, 80,
            90, 90,
            fill="#0b0b0b",
            outline=""
        )