class AICore:

    def __init__(self, canvas):

        self.canvas = canvas

        self.outer = None
        self.core = None
        self.dot = None

        self.size = 0
        self.direction = 1

    def draw(self):

        # Outer Ring
        self.outer = self.canvas.create_oval(
            20, 20,
            150, 150,
            outline="white",
            width=2
        )

        # Main Core
        self.core = self.canvas.create_oval(
            35, 35,
            135, 135,
            fill="white",
            outline=""
        )

        # Center Dot
        self.dot = self.canvas.create_oval(
            80, 80,
            90, 90,
            fill="#0b0b0b",
            outline=""
        )

    def pulse(self):

        if self.size >= 6:
            self.direction = -1

        elif self.size <= 0:
            self.direction = 1

        self.size += self.direction

        self.canvas.coords(
            self.outer,
            20 - self.size,
            20 - self.size,
            150 + self.size,
            150 + self.size
        )

        self.canvas.after(40, self.pulse)