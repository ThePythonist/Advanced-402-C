class Car:
    def __init__(self, model, color, gb):
        self.model = model
        self.color = color
        self.gearbox = gb

    def horn(self):
        print("Hooooooooorn")

    def change_gear(self):
        print("Changed gear")


# Creating Instance ( Object )
dena = Car(model=1402, gb="auto", color="black")
samand = Car(model=1398, gb="manual", color="black")
persia = Car(model=1399, gb="manual", color="white")

# Using Objects
print(dena.color)
print(persia.gearbox)
