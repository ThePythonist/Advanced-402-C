from age import *
import re


def is_vowel(word):
    if re.match(r'^[aeiou]', word, re.IGNORECASE):
        return "an"
    else:
        return "a"


class Human:
    def __init__(self, name, birth, country, job):
        self.name = name
        self.birth = birth
        self.country = country
        self.job = job
        self.age = jalali_age(self.birth)

    def talk(self):
        print(f"""
        Hi I'm {self.name} and I am {self.age} years old.
        I live in {self.country} and I work as {is_vowel(self.job)} {self.job}.""")


class Student(Human):
    def __init__(self, name, birth, country, job, studentid):
        super().__init__(name, birth, country, job)
        self.studentid = studentid

    def entekhab_vahed(self):
        print("Done")


ali = Human("Ali", 1370, "Iran", "Engineer")
saman = Student("Saman", 1377, "Iran", "Baker", "37772342332415")

# ali.talk()
saman.talk()
saman.entekhab_vahed()
print(saman.studentid)
