# Ex: Your own properties
# ---

# create a class Pen
# add at least 3 props
class Pen:
    color = ""
    body_color = ""
    body_material = ""
    pigment = ""
    tip = ""
    brand = ""
    model = ""
    type = ""
    price = 0.0


# create two objects based on class Pen
brush_pen = Pen()
ink_pen = Pen()

# define different props for both objects
# 1. -> brush_pen
brush_pen.color = "black"
brush_pen.body_color = "light brown"
brush_pen.body_material = "plastic"
brush_pen.pigment = "water-based"
brush_pen.tip = "medium"
brush_pen.brand = "Kuretake Bimoji"
brush_pen.model = "XT5-105"
brush_pen.type = "brush"
brush_pen.price = 4.20

# 2. -> ink_pen
ink_pen.color = "blue"
ink_pen.body_color = "black"
ink_pen.body_material = "plastic"
ink_pen.pigment = "pigment-based"
ink_pen.tip = "extra fine"
ink_pen.brand = "UNI"
ink_pen.model = "UNI PIN-03.33"
ink_pen.type = "needle point"
ink_pen.price = 2.45

# display
print(
    "The "
    + ink_pen.model
    + " by "
    + ink_pen.brand
    + " with "
    + ink_pen.tip
    + " tip, will cost you "
    + str(ink_pen.price)
    + "$."
)
print("---")
print(
    "The "
    + brush_pen.model
    + " by "
    + brush_pen.brand
    + " with "
    + brush_pen.tip
    + " tip, will cost you "
    + str(brush_pen.price)
    + "$."
)
print("---")
