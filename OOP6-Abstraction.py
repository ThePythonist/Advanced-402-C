from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14 * self.radius


# Creating instances of the shapes
rectangle = Rectangle(5, 10)
circle = Circle(7)

# Using the abstraction to calculate area and perimeter
print("Rectangle Area:", rectangle.area())  # Output: 50
print("Rectangle Perimeter:", rectangle.perimeter())  # Output: 30
print("Circle Area:", circle.area())  # Output: 153.86
print("Circle Perimeter:", circle.perimeter())  # Output: 43.96
