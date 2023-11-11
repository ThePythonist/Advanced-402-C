class Person:
    def __init__(self, name, age, field, uni):
        self.name = name
        self.age = age
        self.university = uni
        self.field = field

    def talk(self):
        print(f"""
Hi I'm {self.name} and I am {self.age} years old.
I study {self.field} at {self.university}.
        """)


student = Person("Arman", 23, "Computer Engineering", "University of Tehran")
student.talk()
