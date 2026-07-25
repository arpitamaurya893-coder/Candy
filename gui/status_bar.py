import customtkinter as ctk


class StatusBar(ctk.CTkLabel):

    def __init__(self, master):

        super().__init__(
            master,
            text="🤍 Booting...",
            font=("Segoe UI", 18),
            text_color="gray"
        )

    def update_status(self, text):

        self.configure(text=text)