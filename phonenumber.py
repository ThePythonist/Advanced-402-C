import random


def irancell():
    pn = ""
    code = random.choice(["0930", "0939", "0936"])
    for i in range(7):
        pn += str(random.randint(0, 9))

    pn = f"{code}{pn}"
    return pn


def hamrahaval():
    pn = ""
    code = random.choice(["0912", "0993", "0919"])
    for i in range(7):
        pn += str(random.randint(0, 9))

    pn = f"{code}{pn}"
    return pn


def rightell():
    pn = ""
    code = random.choice(["0921", "0923"])
    for i in range(7):
        pn += str(random.randint(0, 9))

    pn = f"{code}{pn}"
    return pn


# print(__name__)

if __name__ == "__main__":
    phonenumbers = []

    for i in range(100):
        phonenumbers.append(irancell() + "\n")

    open("phonebook.txt", "w").writelines(phonenumbers)
    print("Done")
