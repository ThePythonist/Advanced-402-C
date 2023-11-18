import time


class Car:
    def __init__(self, model, color, gb, a):
        self.model = model
        self.color = color
        self.gearbox = gb
        self.speed = 0
        self.acceleration = a

    def horn(self):
        print("Hooooooooorn")

    def change_gear(self):
        print("Changed gear")

    def accelerate(self, value):
        for i in range(value):
            self.speed += 10
            print(self.speed)
            time.sleep(self.acceleration)


# Creating Instance ( Object )
dena = Car(model=1402, gb="auto", color="black", a=1.2)
samand = Car(model=1398, gb="manual", color="black", a=1.6)
persia = Car(model=1399, gb="manual", color="white", a=0.8)

# Using Objects
# print(dena.color)
# print(persia.gearbox)
persia.accelerate(4)
