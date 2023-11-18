class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Cow(Animal):
    def speak(self):
        return "Moo!"


# Create instances of different animals
dog = Dog()
cat = Cat()
cow = Cow()

# Call the speak() method on each animal
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
print(cow.speak())  # Output: Moo!

# -----------------------------------------------------------------------
# Polymorphism in built-in objects

t = (10, 20, 30, 40)
l = [50, 60, 70, 80]

# Call the __len__() method on each instance
print(l.__len__())
print(t.__len__())
