class AICore:

    def __init__(self, canvas):
        self.canvas = canvas

    def draw(self):

        # Outer Ring
        self.canvas.create_oval(
            20, 20,
            150, 150,
            outline="white",
            width=2
        )

        # Main Core
        self.canvas.create_oval(
            35, 35,
            135, 135,
            fill="white",
            outline=""
        )

        # Center Dot
        self.canvas.create_oval(
            80, 80,
            90, 90,
            fill="#0b0b0b",
            outline=""
        )