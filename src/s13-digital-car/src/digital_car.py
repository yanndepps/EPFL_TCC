# Ex: The Digital Car
# ---


class Car:
    # init constructor and props
    def __init__(self, color, brand, transmission, fuel_tank):
        self.color = color
        self.brand = brand
        self.transmission = transmission
        self.fuel_tank = fuel_tank

    # display actual car speed
    def drive(self, speed):
        print("The " + self.brand + " is driving at " + str(speed) + " km/h." + "\n---")

    # display fuel gauge
    def show_fuel(self):
        print(
            "The "
            + self.color
            + " "
            + self.brand
            + " has a fuel reserve which is : "
            + self.fuel_tank
            + "\n---"
        )

    # activate and display lights status
    def activate_lighting(self, toggle):
        if toggle == "on":
            print(
                "The "
                + self.color
                + " "
                + self.brand
                + " with "
                + self.transmission
                + " transmission has active lightings switched on!"
                + "\n---"
            )
        elif toggle == "off":
            print(
                "The "
                + self.color
                + " "
                + self.brand
                + " with "
                + self.transmission
                + " transmission has all lights turned off!"
                + "\n---"
            )


# init object
toyota = Car("red", "Toyota", "manual", "almost empty!")
toyota.drive(88)
toyota.show_fuel()
toyota.activate_lighting("off")

# ---
