# Exercise: Write down actions
# ---


class Pen:
    color = ""
    tip = ""
    type = ""

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
brush_pen = Pen()
brush_pen.color = "Bad Blue Heron"
brush_pen.tip = "Medium"
brush_pen.type = "brush"
brush_pen.draw_circle("Raphaël", 25, "Noodler's Bulletproof")

# init object two
fountain_pen = Pen()
fountain_pen.color = "Charcoal Black"
fountain_pen.tip = "Extra Fine"
fountain_pen.type = "fountain pen"
fountain_pen.draw_line()
