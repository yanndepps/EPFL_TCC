# Exercise: Get building!
# ---

# define class Pen
class Pen:
    def __init__(self, color, tip, type):
        self.color = color
        self.tip = tip
        self.type = type

    def draw_circle(self, brand, diameter, ink):
        print(
            "Pick a "
            + brand
            + " "
            + self.type
            + " and draw a circle with a diameter of "
            + str(diameter)
            + "cm, using the "
            + self.color
            + " color, a "
            + self.tip
            + " tip, and the "
            + ink
            + " ink."
            + "\n---"
        )

    def draw_line(self):
        print(
            "Pick a "
            + self.type
            + " and draw 73 straight lines using a "
            + self.color
            + " color and the "
            + self.tip
            + " tip."
            + "\n---"
        )


# init object one
brush_pen = Pen("Bad Blue Heron", "Medium", "brush")
brush_pen.draw_circle("Raphaël", 25, "Noodle's Bulletproof")

# init object two
fountain_pen = Pen("Charcoal Black", "Extra Fine", "Fountain Pen")
fountain_pen.draw_line()

# ---
