# Inheritance
# class A:
#     def say_hello(self):
#         print("hello")
#
#
# class B(A):
#     def say_goodbye(self):
#         print("goodbye")
#
#
# b = B()
# b.say_goodbye()
# b.say_hello()

# -------------------------------------------------------------------
# Super()
# class Pedar:
#     def __init__(self, fname, address, job):
#         self.familyname = fname
#         self.address = address
#         self.job = job
#
#     def say_hello(self):
#         print("hello")
#
#
# class Farzand(Pedar):
#     def __init__(self, fname, address, uni, job=None):
#         super().__init__(fname, address, job)
#         self.university = uni
#
#     def say_goodbye(self):
#         print("goodbye")
#
#
# pedar = Pedar("ahmadi", "jomhori st", "teacher")
# pesar = Farzand("ahmadi", "jomhori st", "amir kabir university")
# print(pesar.familyname)
# print(pesar.address)
# print(pesar.university)
# -------------------------------------------------------------------
# Without Inheritance
class Pedar:
    def __init__(self, fname="ahmadi"):
        self.familyname = fname

    def greeting(self):
        print("hello")


class Farzand:
    def __init__(self):
        self.pedar = Pedar()

    def say_goodbye(self):
        print("goodbye")


pesar = Farzand()
print(pesar.pedar.greeting())
