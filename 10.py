from math import pi


class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def show_perimeter(self):
        print((self.length + self.width) * 2)

    def show_area(self):
        print(self.length * self.width)


class Circle:
    def __init__(self, r):
        self.radius = r

    def show_perimeter(self):
        print(self.radius * 2 * pi)

    def show_area(self):
        print((self.radius ** 2) * pi)


mostatil = Rectangle(3, 5)
dayere = Circle(3)

mostatil.show_area()
mostatil.show_perimeter()

dayere.show_area()
dayere.show_perimeter()
