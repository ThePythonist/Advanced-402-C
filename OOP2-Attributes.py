class Car:
    # Class Attribute
    shishe = "Doodi"

    def __init__(self):
        self.model = 1402


# Accessing class attribute
# print(Car.shishe)

# Creating instances
persia = Car()
dena = Car()

# Accessing instance attribute
print(persia.model)
print(dena.model)

# Modifying instance attribute
persia.model = 1403
print(persia.model)
print(dena.model)

# Modifying class attribute
Car.shishe = "Adi"
print(persia.shishe)
print(dena.shishe)
